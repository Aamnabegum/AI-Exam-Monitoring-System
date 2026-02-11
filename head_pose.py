import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# --- Smoothing memory ---
previous_horizontal = 0
previous_vertical = 0

def detect_head_direction(frame):
    global previous_horizontal, previous_vertical

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return "No Face"

    landmarks = results.multi_face_landmarks[0]
    h, w, _ = frame.shape

    # Draw face mesh
    mp_drawing.draw_landmarks(
        frame,
        landmarks,
        mp_face_mesh.FACEMESH_CONTOURS,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp_drawing.DrawingSpec(
            color=(0,255,0), thickness=1, circle_radius=1
        )
    )

    # Key landmarks
    nose = landmarks.landmark[1]
    left_eye = landmarks.landmark[33]
    right_eye = landmarks.landmark[263]
    chin = landmarks.landmark[152]

    nose_x = nose.x * w
    nose_y = nose.y * h
    left_eye_x = left_eye.x * w
    right_eye_x = right_eye.x * w
    chin_y = chin.y * h

    # Draw nose marker
    cv2.circle(frame, (int(nose_x), int(nose_y)), 5, (0,0,255), -1)

    eye_center_x = (left_eye_x + right_eye_x) / 2

    # Raw ratios
    horizontal_ratio = (nose_x - eye_center_x) / w
    vertical_ratio = (chin_y - nose_y) / h

    # --- Apply smoothing ---
    alpha = 0.7   # Higher = smoother (less jitter)
    horizontal_ratio = alpha * previous_horizontal + (1 - alpha) * horizontal_ratio
    vertical_ratio = alpha * previous_vertical + (1 - alpha) * vertical_ratio

    previous_horizontal = horizontal_ratio
    previous_vertical = vertical_ratio

    # --- Debug display (for tuning) ---
    cv2.putText(frame, f"H: {round(horizontal_ratio,3)}",
                (20,140),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (255,255,0), 2)

    # --- Improved thresholds ---
    if horizontal_ratio > 0.035:
        return "Looking Right - Suspicious"
    elif horizontal_ratio < -0.035:
        return "Looking Left - Suspicious"
    elif vertical_ratio > 0.30:
        return "Looking Down - Suspicious"
    else:
        return "Looking Forward"

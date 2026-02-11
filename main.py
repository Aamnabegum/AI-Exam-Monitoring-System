import cv2
import datetime
import time
from head_pose import detect_head_direction


def run_exam():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    suspicious_count = 0
    suspicious_start_time = None
    suspicious_threshold = 0.5
    cooldown_time = 1.5
    last_detection_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        current_time = time.time()

        # Display Title
        cv2.putText(frame, "AI Exam Monitoring System",
                    (20, 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255, 255, 255), 2)

        # Detect Head Direction
        status = detect_head_direction(frame)

        cv2.putText(frame, status, (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)

        # Suspicious Logic
        if "Suspicious" in status:

            if suspicious_start_time is None:
                suspicious_start_time = current_time

            elif (current_time - suspicious_start_time >= suspicious_threshold) and \
                 (current_time - last_detection_time >= cooldown_time):

                suspicious_count += 1
                last_detection_time = current_time
                suspicious_start_time = None

                with open("suspicious_log.txt", "a") as file:
                    file.write(f"{datetime.datetime.now()} - {status}\n")

        else:
            suspicious_start_time = None

        # Display Counter
        cv2.putText(frame, f"Suspicious Count: {suspicious_count}",
                    (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2)

        cv2.imshow("Exam Monitoring System", frame)

        # Press Q to end exam
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return suspicious_count

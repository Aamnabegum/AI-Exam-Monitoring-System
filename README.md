# 🧠 AI-Based Exam Monitoring System

An intelligent real-time proctoring system that detects suspicious head movements during online examinations using Computer Vision and Flask-based web integration.

---

## 🚀 Project Overview

This system monitors a student through webcam during an online test and detects suspicious head movements such as:

- Looking Left
- Looking Right
- (Optional extension: Looking Up / Down)

The suspicious activity count is recorded and stored in a database. An admin panel allows faculty to view exam results and suspicious activity reports.

---

## 🎯 Features

✅ Real-time face tracking using MediaPipe  
✅ Head direction detection using facial landmarks  
✅ Suspicious activity counter with time threshold logic  
✅ Flask-based login system  
✅ Role-based access (Student / Admin)  
✅ SQLite database integration  
✅ Admin dashboard to view student results  
✅ Git version controlled project  

---

## 🏗️ System Architecture

Student Login
↓
Flask Backend (app.py)
↓
AI Monitoring Engine (main.py)
↓
Head Pose Detection (head_pose.py)
↓
Suspicious Activity Count
↓
Stored in SQLite Database
↓
Admin Dashboard View


---

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- Flask
- SQLite
- HTML (Basic Frontend)
- Git & GitHub

---

## 📂 Project Structure

EXAMPROJECT/
│
├── app.py
├── main.py
├── head_pose.py
├── face_detection.py
├── behavior_analysis.py
├── templates/
├── requirements.txt
└── .gitignore


---

## ⚙️ Installation & Setup

1. Clone the repository:



git clone https://github.com/Aamnabegum/AI-Exam-Monitoring-System.git

cd AI-Exam-Monitoring-System


2. Create virtual environment:



python -m venv .venv


3. Activate environment:

Windows:


..venv\Scripts\activate


4. Install dependencies:



pip install -r requirements.txt


5. Run the application:



python app.py


6. Open browser and go to:



http://127.0.0.1:5000


---

## 👤 Demo Credentials

Student:
- Username: student1
- Password: 123

Admin:
- Username: admin
- Password: admin123

---

## 📌 Future Improvements

- Eye movement detection
- Face absence detection
- Multiple face detection
- Video recording storage
- Cloud deployment
- AI-based cheating classification using ML model

---

## 📚 Educational Purpose

This project is developed as a Mini Project for academic demonstration of:

- Computer Vision
- AI Integration
- Backend Development
- Database Handling
- Real-Time Systems

---

## ✨ Author

Aamna Begum  
B.Tech Student  
Aspiring AI & Data Science Professional

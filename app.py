from flask import Flask, render_template, request, redirect
import sqlite3
from main import run_exam

app = Flask(__name__)

# Create database tables if not exists
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        suspicious_count INTEGER
    )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        if user[3] == "admin":
            return redirect("/admin")
        else:
            return render_template("dashboard.html", username=username)
    else:
        return "Invalid credentials"


@app.route("/start_exam", methods=["POST"])
def start_exam():
    username = request.form["username"]

    count = run_exam()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (username, suspicious_count) VALUES (?, ?)", (username, count))
    conn.commit()
    conn.close()

    return render_template("result.html", count=count)


@app.route("/admin")
def admin():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM results")
    data = cursor.fetchall()
    conn.close()

    return render_template("admin.html", data=data)


if __name__ == "__main__":
    print("Starting AI Exam Monitoring System...")
    print("Open browser and go to: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)


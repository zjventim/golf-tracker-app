import sqlite3
import os

DB_PATH = os.path.join("data", "golf.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def insert_round(course_id, date, score):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO rounds (course_id, date, score) VALUES (?, ?, ?)",
        (course_id, date, score)
    )
    conn.commit()
    conn.close()

def get_rounds():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM rounds ORDER BY date DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

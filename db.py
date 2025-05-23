from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

DB_PATH = os.path.join("data", "golf.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

# Create table for user
def create_user_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL     
        )
    ''')
    conn.commit()
    conn.close()

# Insert statement functions
def insert_round(course_id, date, score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO rounds (course_id, date, score) VALUES (?, ?, ?)",
        (course_id, date, score)
    )
    conn.commit()
    conn.close()

def get_rounds():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rounds ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def create_user(username, password):
    conn = get_connection()
    cur = conn.cursor()
    hashed = generate_password_hash(password)
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
    conn.commit()
    conn.close()

def get_user_by_username(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cur.fetchone()
    conn.close()
    return user

def validate_login(username, password):
    user = get_user_by_username(username)
    if user and check_password_hash(user[2], password):  # user[2] = hashed pw
        return user
    return None

def get_user_by_id(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cur.fetchone()
    conn.close()
    return user
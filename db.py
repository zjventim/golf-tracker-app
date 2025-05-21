import sqlite3

def get_connection():
    conn = sqlite3.connect('data/golf.db')
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            name TEXT,
            rating REAL,
            slope INTEGER,
            par INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rounds (
            id INTEGER PRIMARY KEY,
            course_id INTEGER,
            date TEXT,
            score INTEGER,
            FOREIGN KEY(course_id) REFERENCES courses(id)
        )
    ''')

    conn.commit()
    conn.close()
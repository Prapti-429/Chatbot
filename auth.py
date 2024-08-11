# auth.py

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    user_id = str(uuid.uuid4())
    try:
        cursor.execute('INSERT INTO users (id, username, password) VALUES (?, ?, ?)', (user_id, username, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False
    conn.close()
    return True

def login_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password_hash(user[1], password):
        session_id = str(uuid.uuid4())
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO sessions (session_id, user_id) VALUES (?, ?)', (session_id, user[0]))
        conn.commit()
        conn.close()
        return session_id
    return None

def validate_session(session_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM sessions WHERE session_id = ?', (session_id,))
    session = cursor.fetchone()
    conn.close()
    return session is not None

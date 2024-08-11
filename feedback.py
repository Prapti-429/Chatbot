# feedback.py

import sqlite3

# Initialize SQLite database for feedback
def init_feedback_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            feedback TEXT NOT NULL,
            rating INTEGER CHECK(rating BETWEEN 1 AND 5),
            FOREIGN KEY(session_id) REFERENCES sessions(session_id)
        )
    ''')
    conn.commit()
    conn.close()

def record_feedback(session_id, feedback, rating):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO feedback (session_id, feedback, rating) VALUES (?, ?, ?)', (session_id, feedback, rating))
    conn.commit()
    conn.close()

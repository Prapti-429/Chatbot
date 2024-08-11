# auth.py
# auth.py

import json
import uuid
from hashlib import sha256

# File to store user data
USER_DATA_FILE = 'user_data.json'
SESSION_FILE = 'sessions.json'

def load_user_data():
    """Load user data from the file."""
    try:
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(user_data):
    """Save user data to the file."""
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(user_data, file)

def load_sessions():
    """Load active sessions from the file."""
    try:
        with open(SESSION_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_sessions(sessions):
    """Save active sessions to the file."""
    with open(SESSION_FILE, 'w') as file:
        json.dump(sessions, file)

def hash_password(password):
    """Hash the password using SHA-256."""
    return sha256(password.encode()).hexdigest()

def register_user(username, password):
    """Register a new user."""
    user_data = load_user_data()
    
    if username in user_data:
        return False  # User already exists
    
    hashed_password = hash_password(password)
    user_data[username] = hashed_password
    save_user_data(user_data)
    return True

def login_user(username, password):
    """Log in a user and return a session ID if successful."""
    user_data = load_user_data()
    hashed_password = hash_password(password)
    
    if username in user_data and user_data[username] == hashed_password:
        session_id = str(uuid.uuid4())
        sessions = load_sessions()
        sessions[session_id] = username
        save_sessions(sessions)
        return session_id
    return None

def validate_session(session_id):
    """Validate the session ID."""
    sessions = load_sessions()
    return sessions.get(session_id)

def logout_user(session_id):
    """Log out a user by invalidating the session ID."""
    sessions = load_sessions()
    if session_id in sessions:
        del sessions[session_id]
        save_sessions(sessions)
        return True
    return False

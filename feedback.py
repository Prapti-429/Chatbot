# feedback.py

import json

# File to store feedback data
FEEDBACK_FILE = 'feedback_data.json'

def load_feedback_data():
    """
    Load feedback data from the file.
    """
    try:
        with open(FEEDBACK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_feedback_data(feedback_data):
    """
    Save feedback data to the file.
    """
    with open(FEEDBACK_FILE, 'w') as file:
        json.dump(feedback_data, file, indent=4)

def record_feedback(session_id, feedback, rating):
    """
    Record feedback provided by the user.
    """
    feedback_data = load_feedback_data()
    
    feedback_entry = {
        'session_id': session_id,
        'feedback': feedback,
        'rating': rating
    }
    
    feedback_data.append(feedback_entry)
    save_feedback_data(feedback_data)
    print("Thank you for your feedback!")

def get_feedback_summary():
    """
    Retrieve and summarize feedback data.
    """
    feedback_data = load_feedback_data()
    
    if not feedback_data:
        return "No feedback available."
    
    summary = {
        'total_feedback': len(feedback_data),
        'average_rating': sum(entry['rating'] for entry in feedback_data) / len(feedback_data)
    }
    
    return summary

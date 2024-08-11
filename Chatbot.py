# chatbot.py

import openai
from router import route_query
from translator import detect_language, translate_to_english, translate_to_original
from auth import register_user, login_user, validate_session
from feedback import record_feedback
from models import generate_response, get_knowledge_base_response

# Setup OpenAI API key (Replace with your actual OpenAI API key)
openai.api_key = 'your-openai-api-key'

def authenticate():
    """
    Handles user authentication. Users can register or log in.
    Returns a session ID if login is successful.
    """
    print("1. Register")
    print("2. Login")
    choice = input("Choose an option: ")
    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        if register_user(username, password):
            print("Registration successful!")
            return None
        else:
            print("Username already exists.")
            return None
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        session_id = login_user(username, password)
        if session_id:
            print("Login successful!")
            return session_id
        else:
            print("Invalid credentials.")
            return None
    return None

def handle_rag_query(query):
    """
    Handles Retrieval-Augmented Generation (RAG) queries using a knowledge base.
    """
    response = get_knowledge_base_response(query)
    return response

def generate_llm_response(query):
    """
    Generates a response using a Generative AI Model (LLM).
    """
    response = generate_response(query)
    return response

def get_feedback():
    """
    Prompts the user to provide feedback and a rating.
    """
    feedback = input("Please provide your feedback: ")
    rating = int(input("Rate the response (1 to 5): "))
    return feedback, rating

def main():
    """
    Main function to run the chatbot application.
    Handles user interaction, language translation, and feedback collection.
    """
    session_id = authenticate()
    if not session_id:
        return

    print("Welcome to the Personalized Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Detect the language of the user input
        language = detect_language(user_input)
        
        # If the language is not English, translate it to English
        if language != 'en':
            translated_input = translate_to_english(user_input)
        else:
            translated_input = user_input
        
        # Route the query to the appropriate handler
        if "knowledge" in translated_input.lower():
            response = handle_rag_query(translated_input)
        else:
            response = generate_llm_response(translated_input)
        
        # If the original language was not English, translate the response back
        if language != 'en':
            response = translate_to_original(response, language)
        
        print("Bot:", response)
        
        # Collect feedback from the user
        feedback, rating = get_feedback()
        record_feedback(session_id, feedback, rating)

if __name__ == '__main__':
    main()

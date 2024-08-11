def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I assist you today?",
        "how are you?": "I'm just a bot, but I'm functioning as expected! How about you?",
        "what's your name?": "I'm a simple chatbot created by Prapti!",
        "bye": "Goodbye! Feel free to chat with me anytime."
    }
    
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("Bot:", response)


def chatbot_response(user_input):
    positive_responses = ["Great!", "Awesome!", "Glad to hear that!"]
    negative_responses = ["Oh no!", "I'm sorry to hear that.", "That's unfortunate."]
    if "good" in user_input.lower() or "happy" in user_input.lower():
        return random.choice(positive_responses)
    elif "bad" in user_input.lower() or "sad" in user_input.lower():
        return random.choice(negative_responses)
    else:
        responses = {
            "hi": "Hello! How can I assist you today?",
            "how are you?": "I'm just a bot, but I'm functioning as expected! How about you?",
            "bye": "Goodbye! Feel free to chat with me anytime."
        }
        return responses.get(user_input.lower(), "Sorry, I don't understand that.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("Bot:", response)

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hi" in user_input or "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing well! How about you?"
    elif "your name" in user_input:
        return "I'm a chatbot created by Prapti!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that."
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("Bot:", response)

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hi" in user_input or "hello" in user_input:
        return "Hello! How are you today?"
    elif "how are you" in user_input:
        return "I'm doing well, thank you! What about you?"
    elif "good" in user_input or "fine" in user_input:
        return "Great to hear! Is there anything you'd like to ask me?"
    elif "bad" in user_input or "not good" in user_input:
        return "I'm sorry to hear that. Would you like to talk about it?"
    elif "bye" in user_input:
        return "Goodbye! Take care!"
    else:
        return "I'm not sure how to respond to that. Could you please clarify?"
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("Bot:", response)

import openai

# Set your OpenAI API key here
openai.api_key = 'your-openai-api-key'

def chatbot_response(user_input):
    try:

        response = openai.Completion.create(
            engine="text-davinci-003",  # Use "gpt-4" if you have access
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "I'm sorry, I couldn't process your request."

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("Bot:", response)

import openai
from transformers import AutoTokenizer, AutoModel
import faiss
import numpy as np


openai.api_key = 'your-openai-api-key'

# Knowledge base - This is a simple example. You can expand this as needed.
knowledge_base = [
    "Python is a high-level programming language.",
    "Flask is a micro web framework written in Python.",
    "AWS EC2 is a service that provides scalable computing capacity in the cloud.",
    "OpenAI's GPT models are used for generating human-like text."
]

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")


def embed_texts(texts):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.detach().numpy()


embeddings = embed_texts(knowledge_base)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def retrieve_passages(query, k=1):
    query_embedding = embed_texts([query])
    distances, indices = index.search(query_embedding, k)
    return [knowledge_base[i] for i in indices[0]]

def chatbot_response(user_input):
    relevant_passages = retrieve_passages(user_input)
    prompt = f"Based on the following information:\n{relevant_passages[0]}\n\nQ: {user_input}\nA:"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use "gpt-4" if you have access
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot_response(user_input)
        print("Bot:", response)

# chatbot.py

from router import route_query

if __name__ == '__main__':
    print("Welcome to the Orchestrated Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = route_query(user_input)
        print("Bot:", response)

# chatbot.py

from router import route_query
from translator import detect_language, translate_to_english, translate_to_original

if __name__ == '__main__':
    print("Welcome to the Multi-Language Orchestrated Chatbot! Type 'exit' to quit.")
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
        
        # Route the query and get the response
        response = route_query(translated_input)
        
        # If the original language was not English, translate the response back
        if language != 'en':
            response = translate_to_original(response, language)
        
        print("Bot:", response)

# chatbot.py

from router import route_query
from translator import detect_language, translate_to_english, translate_to_original
from auth import register_user, login_user, validate_session

def authenticate():
    print("1. Register")
    print("2. Login")
    choice = input("Choose an option: ")
    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        if register_user(username, password):
            print("Registration successful!")
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

def main():
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
        
        # Route the query and get the response
        response = route_query(translated_input)
        
        # If the original language was not English, translate the response back
        if language != 'en':
            response = translate_to_original(response, language)
        
        print("Bot:", response)

if __name__ == '__main__':
    main()

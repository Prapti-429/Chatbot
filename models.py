# models.py

import openai
import json

# Setup OpenAI API key
openai.api_key = 'your-openai-api-key'

# Path to the knowledge base JSON file
KNOWLEDGE_BASE_FILE = 'knowledge_base.json'

def load_knowledge_base():
    """
    Load the knowledge base from a JSON file.
    """
    try:
        with open(KNOWLEDGE_BASE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_knowledge_base(knowledge_base):
    """
    Save the knowledge base to a JSON file.
    """
    with open(KNOWLEDGE_BASE_FILE, 'w') as file:
        json.dump(knowledge_base, file)

def generate_response(query):
    """
    Generate a response using OpenAI's GPT model.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use any model you prefer
        prompt=query,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def get_knowledge_base_response(query):
    """
    Retrieve a response from the knowledge base based on the query.
    """
    knowledge_base = load_knowledge_base()
    response = knowledge_base.get(query.lower(), "Sorry, I don't have information on that topic.")
    return response

def add_knowledge_base_entry(query, response):
    """
    Add or update an entry in the knowledge base.
    """
    knowledge_base = load_knowledge_base()
    knowledge_base[query.lower()] = response
    save_knowledge_base(knowledge_base)

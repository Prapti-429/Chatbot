# models.py

import openai

openai.api_key = 'your-openai-api-key'

def fact_model(query):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use "gpt-4" if you have access
        prompt=f"Answer the following factual question: {query}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

def creative_model(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Create a creative response: {query}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def sentiment_model(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the sentiment of the following text: {query}",
        max_tokens=50
    )
    return response.choices[0].text.strip()
openai.api_key = 'your-openai-api-key'

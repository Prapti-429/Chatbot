# Chatbot Project
This project is a basic chatbot that uses OpenAI's GPT model to generate intelligent responses.

## Setup

1. Install the necessary Python packages:

2. Set your OpenAI API key in `chatbot.py`:
```python
openai.api_key = 'your-openai-api-key'

python chatbot.py

# Chatbot Project with RAG Implementation

This project is a chatbot that uses OpenAI's GPT model, augmented with a retrieval mechanism to generate intelligent responses based on a specific knowledge base.

## New Features

- **Retrieval-Augmented Generation (RAG):** The chatbot can now retrieve relevant passages from a predefined knowledge base and use them to generate contextually accurate responses.

## Setup

1. Install the necessary Python packages:

2. Set your OpenAI API key in `chatbot.py`:
```python
openai.api_key = 'your-openai-api-key'

# Chatbot Project with LLM Orchestration

This project is a chatbot that uses OpenAI's GPT model, enhanced with a router that directs user queries to specific task-based models.

## Features

- **Retrieval-Augmented Generation (RAG):** Retrieve and generate responses based on a predefined knowledge base.
- **LLM Orchestration:** Route queries to task-specific models based on the nature of the query (e.g., factual, creative, sentiment analysis).

## Setup

1. Install the necessary Python packages:

2. Set your OpenAI API key in `models.py`:
```python
openai.api_key = 'your-openai-api-key'

python chatbot.py

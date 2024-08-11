# router.py

from models import fact_model, creative_model, sentiment_model

def route_query(user_input):
    # Simple keyword-based routing logic (can be replaced with more advanced logic)
    if any(keyword in user_input.lower() for keyword in ['who', 'what', 'when', 'where', 'why', 'how']):
        return fact_model(user_input)
    elif any(keyword in user_input.lower() for keyword in ['create', 'write', 'imagine']):
        return creative_model(user_input)
    elif any(keyword in user_input.lower() for keyword in ['feel', 'emotion', 'sentiment']):
        return sentiment_model(user_input)
    else:
        return "Sorry, I can't handle this query. Please rephrase or try a different question."

if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = route_query(user_input)
        print("Bot:", response)

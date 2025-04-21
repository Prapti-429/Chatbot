touch chatbot.py
def chatbot_response(user_input):
    responses = {
        "hi": "Hello!",
        "how are you?": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a great day!"
    }
    
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

# Simulate a conversation
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
python chatbot.py

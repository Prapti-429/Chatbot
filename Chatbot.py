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


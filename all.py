# Define the rules for the AI agent
rules = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "default": "I'm sorry, I don't understand that."
}

# Create the AI agent function
def ai_agent(user_input):
    user_input = user_input.lower()
    return rules.get(user_input, rules["default"])

# Test the AI agent
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI: Goodbye!")
            break
        response = ai_agent(user_input)
        print(f"AI: {response}")

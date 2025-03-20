# M20
Gen AI

simple example of a basic AI agent using Python. This agent will make decisions based on a set of predefined rules. For this example, we'll create a simple chatbot that responds to greetings and farewells.

Step 1: Define the Rules
Create a dictionary to define the responses for different inputs.

Python
# Define the rules for the AI agent
rules = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "default": "I'm sorry, I don't understand that."
}
Step 2: Create the AI Agent Function
Create a function that takes user input and returns a response based on the rules.

Python
def ai_agent(user_input):
    user_input = user_input.lower()
    return rules.get(user_input, rules["default"])
Step 3: Test the AI Agent
Test the AI agent with different inputs.

Python
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI: Goodbye!")
            break
        response = ai_agent(user_input)
        print(f"AI: {response}")
Complete Code
Here is the complete code:

Python
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
This is a very basic AI agent that uses simple pattern matching. For more complex AI agents, you can explore natural language processing (NLP) libraries such as NLTK or spaCy, and machine learning frameworks like TensorFlow or PyTorch.

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI: Goodbye!")
            break
        response = ai_agent(user_input)
        print(f"AI: {response}")

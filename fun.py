def ai_agent(user_input):
    user_input = user_input.lower()
    return rules.get(user_input, rules["default"])

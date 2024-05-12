import re
from datetime import datetime
import random

def simple_chatbot(user_input):
    responses = {
        r'\bhello\b': "Hello! How can I help you?",
        r'\bwho are you\b': "I'm a chatbot, and I'm here to assist you!",
        r'\bwho is your boss\b': "Saksham is my boss!",
        r'\bwhat can you do here\b': "I'm a chatbot, and I'm here to assist you!",
        r'\bbye\b': "Goodbye! Have a great day!",
        r'\btime\b': f"The current time is {datetime.now().strftime('%H:%M')}.",
        r'\bdate\b': f"Today's date is {datetime.now().strftime('%Y-%m-%d')}.",
        r'\bquit\b': "Chatbot: Goodbye! Thanks for chatting with me.",
        r'\bjoke\b': "Here's a joke for you: Why don't scientists trust atoms? Because they make up everything!",
        r'\bcalculate\b': calculate,
        r'\bweather\b': "I'm just a chatbot and cannot check the weather at the moment. Sorry!",
        r'\b(?:how.*)\b(?:you.*)\b(?:help.*)\b': "I can assist you with various tasks such as providing information, telling jokes, and performing calculations."
    }

    for pattern, reply in responses.items():
        if re.search(pattern, user_input, re.I):
            if callable(reply):
                return reply(user_input)
            return reply

    return "I'm sorry, I don't understand that."

def calculate(user_input):
    match = re.search(r'(\d+)\s*([-+*\/])\s*(\d+)', user_input, re.I)
    if match:
        num1 = float(match.group(1))
        operator = match.group(2)
        num2 = float(match.group(3))
        if operator == '+':
            return f"The result of {num1} {operator} {num2} is {num1 + num2}."
        elif operator == '-':
            return f"The result of {num1} {operator} {num2} is {num1 - num2}."
        elif operator == '*':
            return f"The result of {num1} {operator} {num2} is {num1 * num2}."
        elif operator == '/':
            if num2 != 0:
                return f"The result of {num1} {operator} {num2} is {num1 / num2}."
            else:
                return "Cannot divide by zero!"
    else:
        return "Sorry, I couldn't understand the calculation request."

def main():
    print("Chatbot: Hello! You can type 'quit' or 'exit' if you want to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Chatbot: Goodbye! Thanks for chatting with me.")
            break

        response = simple_chatbot(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()

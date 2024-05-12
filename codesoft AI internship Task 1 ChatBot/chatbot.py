import re
from datetime import datetime

def simplechatbot(user_input):
    responses = {
        r'\bhello\b': "Hello! How can I help you?",
        r'\bwho are you\b': "I'm a chatbot, and I'm here to assist you!",
        r'\bwho is your boss\b': "SAKSHAM is my boss!",
        r'\bbye\b': "Goodbye! Have a great day!",
        r'\btime\b': f"The current time is {datetime.now().strftime('%H:%M')}.",
        r'\bdate\b': f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."
    }

    for pattern, reply in responses.items():
        if re.search(pattern, user_input, re.I):
            return reply

    return "I'm sorry, I don't understand that."

def main():
    print("Chatbot: Hello! You can type 'exit' if you want to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = simplechatbot(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()

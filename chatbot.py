def chatbot():
    print("🤖 Welcome to ChatBot!")
    print("💬 You can talk to me. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello there! 👋")
        elif user_input in ["how are you", "how are you doing"]:
            print("Bot: I'm doing great, thanks for asking! 😊")
        elif user_input in ["what is your name", "who are you"]:
            print("Bot: I'm a simple rule-based chatbot built with Python.")
        elif user_input in ["what can you do", "help"]:
            print("Bot: I can reply to basic greetings and questions. Try saying 'hello', 'how are you', or 'bye'.")
        elif user_input in ["thank you", "thanks"]:
            print("Bot: You're welcome! 🙌")
        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day! 👋")
            break
        elif user_input in ["what is the time", "tell me the time"]:
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"Bot: The current time is {current_time}. ⏰")
        elif user_input in ["what's the weather", "how's the weather"]:
            print("Bot: I'm not connected to the internet, so I can't tell the weather right now. 🌤")
        else:
            print("Bot: I'm not sure how to respond to that. 🤔 Try saying 'help'.")

# Run the chatbot
chatbot()
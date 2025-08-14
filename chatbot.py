def simple_chatbot():
    print("Chatbot: Hi there! I'm a simple chatbot. How can I help you today?") # Initial greeting

    while True: # Keep the conversation going until the user exits
        user_input = input("You: ").lower() # Get user input and convert to lowercase for case-insensitive matching

        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break # Exit the loop and end the conversation
        elif "hello" in user_input:
            print("Chatbot: Hello! How can I assist you today?") # Respond to greetings
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm here to help you!")
        elif "weather" in user_input:
            print("Chatbot: I'm sorry, I don't have access to real-time weather information.")
        elif "joke" in user_input:
            print("Chatbot: Why did the scarecrow win an award? Because he was outstanding in his field!")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?") # Catch-all response for unknown input

if __name__ == "__main__":
    simple_chatbot()

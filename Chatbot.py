def chatbot():
    print("Bot: Hello! I am simple chatbopt.")
    print("Bot: Type 'bye'to exit the chat")

    while True:
        user =input("You:").lower()

        if "hello" in user or "hi" in user:
            print("Bot:Hello! How can i help you?")

        elif "name" in user:
            print("Bot:I am a simple Python chatbot.")

        elif"how are you" in user:
            print ("Bot: I am fine , Thank you!") 

        elif"ai" in user:
            print("Bot:AI stand for Artificial Intelligence.It is a firld of computer science.")

        elif "bye" in user:
            print("Bot:Goodbye ! Have a great day!")
            break 

        else:
            print("Bot:I am sorry, I don't understand that.")


chatbot()


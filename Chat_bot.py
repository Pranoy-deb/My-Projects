def simlle_chatbot():
    responses = {
        "hello":"Hi there! How can I help you?",
        "how are you":"I'm just a computer program, but thanks for asking!",
        "what is your name": "I am a chatbot.",
        "what is python": "Python is a popular programming language.",
        "bye": "Goodbye! Have a great day!"
    }
    print("Simple Chatbot: Hello! Type 'bye' to exit")

    while True:
        user_input = input("You: ").lower()
        if user_input =="bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif user_input in responses:
            print("Simple Chatbot: ",responses[user_input])
        else:
            print("Simple Chatbot: I am sorry, I don'n understand that.")
simlle_chatbot()
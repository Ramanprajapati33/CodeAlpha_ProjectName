def get_reply(message):
    message = message.strip().lower()

    if message in {"hello", "hi", "hey"}:
        return "Hi! How can I help you?"
    if message in {"how are you", "how are you?"}:
        return "I'm fine, thanks! How are you?"
    if message in {"i am fine", "i'm fine", "fine"}:
        return "Glad to hear that!"
    if message in {"what is your name", "what is your name?"}:
        return "I'm a simple Python rule-based chatbot."
    if message in {"help", "what can you do"}:
        return "You can greet me, ask how I am, ask my name, or say bye."
    if message in {"bye", "goodbye", "exit", "quit"}:
        return None
    return "Sorry, I don't understand that yet. Try 'hello', 'how are you', 'help', or 'bye'."


def main():
    print("=== Basic Chatbot ===")
    print("Type 'bye' to end the conversation.")

    while True:
        user_message = input("You: ")
        reply = get_reply(user_message)
        if reply is None:
            print("Bot: Goodbye!")
            break
        print(f"Bot: {reply}")


if __name__ == "__main__":
    main()

def show_messages(messages):
    print("Messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    print("\nSending messages...")
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
        print(current_message)
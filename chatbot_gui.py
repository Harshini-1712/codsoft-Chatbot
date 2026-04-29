import datetime
import random
import tkinter as tk
from tkinter import scrolledtext

# Bot logic
def chatbot_response(user):
    user = user.lower()

    if "hi" in user or "hello" in user or "hey" in user :
        return "Hello! How can I help you? 😊"

    elif "name" in user:
        return "I am a simple rule-based chatbot."

    elif "how are you" in user:
        return "I am doing great! Thanks for asking 😄"

    elif "time" in user:
        return "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")

    elif "date" in user:
        return "Today's date is " + str(datetime.date.today())

    elif "joke" in user:
        jokes = [
            "Why did the computer sleep? Because it was tired 😂",
            "Why do programmers hate nature? Too many bugs 🐛",
            "Why did the laptop go to doctor? It had a virus 😷"
        ]
        return random.choice(jokes)

    elif "bye" in user:
        return "Bye! Take care 👋"

    elif "thanks" in user or "thank you" in user:
        return "You're welcome 😊"

    elif "good morning" in user:
        return "Good morning! ☀️"

    elif "good night" in user:
        return "Good night 😴"

    else:
        return "Sorry, I didn't understand 😅"


# Send message
def send_message():
    user_input = entry_box.get()

    if user_input.strip() == "":
        return

    chat_area.insert(tk.END, "You: " + user_input + "\n", "user")

    response = chatbot_response(user_input)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n", "bot")

    chat_area.yview(tk.END)  # auto scroll
    entry_box.delete(0, tk.END)


# Clear chat
def clear_chat():
    chat_area.delete('1.0', tk.END)


# GUI window
window = tk.Tk()
window.title("Simple Chatbot 🤖")
window.geometry("400x500")
window.configure(bg="lightblue")

# Chat area
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20)
chat_area.pack(padx=10, pady=10)

# Colors
chat_area.tag_config("user", foreground="blue")
chat_area.tag_config("bot", foreground="green")

# Input box
entry_box = tk.Entry(window, width=30)
entry_box.pack(padx=10, pady=5)
entry_box.insert(0, "Type your message here...")

# Enter key support
entry_box.bind("<Return>", lambda event: send_message())

# Buttons
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear Chat", command=clear_chat)
clear_button.pack(pady=5)

exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.pack(pady=5)

# Run app
window.mainloop()
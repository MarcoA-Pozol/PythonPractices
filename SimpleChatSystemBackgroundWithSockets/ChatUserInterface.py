import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Client socket setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8600))

# Get Username
username = input("Enter your username: ")

# GUI setup
root = tk.Tk()
root.title("Chat App")
root.geometry("400x500")

# Label for the person you're chatting with (larger font)
chatting_with_label = tk.Label(root, text="Chatting with: Unknown", font=("Arial", 14, "bold"), fg="blue")
chatting_with_label.pack(pady=5)

# Chat window
chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entry field for messages
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)
message_entry.bind("<Return>", lambda event: send_message())  # Send message on Enter key

# Send button
send_button = tk.Button(root, text="Send", command=lambda: send_message())
send_button.pack(pady=5)

def receive_messages():
    """Continuously receive messages from the server and display them with color formatting."""
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            
            if not msg:
                continue

            sender_name = msg.split(":")[0]  # Extract sender's name
            message_text = msg[len(sender_name) + 2:]  # Extract the actual message

            chat_window.config(state=tk.NORMAL)

            # Display the sender's name in RED and the message in BLACK
            chat_window.insert(tk.END, sender_name + ": ", "sender")  # Colored username
            chat_window.insert(tk.END, message_text + '\n', "message")  # Normal text

            chat_window.config(state=tk.DISABLED)
            chat_window.yview(tk.END)  # Auto-scroll

            # Update the "Chatting with" label dynamically (if it's a new user)
            if sender_name != username:
                chatting_with_label.config(text=f"Chatting with: {sender_name}")

        except ConnectionResetError:
            break

def send_message():
    """Send message to the server."""
    msg = message_entry.get()
    if msg:
        client.send(f'{username}: {msg}'.encode('utf-8'))

        chat_window.config(state=tk.NORMAL)

        # Display your own message in BLUE
        chat_window.insert(tk.END, "You: ", "you")  # 'You' label in blue
        chat_window.insert(tk.END, msg + '\n', "message")  # Message in black

        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)  # Auto-scroll
        message_entry.delete(0, tk.END)

# Text styling
chat_window.tag_configure("sender", foreground="red", font=("Arial", 10, "bold"))  # Other user in RED
chat_window.tag_configure("you", foreground="blue", font=("Arial", 10, "bold"))  # Your messages in BLUE
chat_window.tag_configure("message", foreground="black", font=("Arial", 10))  # Normal message text

# Start receiving messages
threading.Thread(target=receive_messages, daemon=True).start()

root.mainloop()
client.close()

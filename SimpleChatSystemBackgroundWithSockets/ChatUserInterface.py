import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Client socket setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8600))

def receive_messages():
    """Continuously receive messages from the server and display them."""
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, msg + '\n')
            chat_window.config(state=tk.DISABLED)
            chat_window.yview(tk.END)  # Auto-scroll
        except ConnectionResetError:
            break

def send_message():
    """Send message to the server."""
    msg = message_entry.get()
    if msg:
        client.send(f'{username}: {msg}'.encode('utf-8'))
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f'You: {msg}\n')
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)  # Auto-scroll
        message_entry.delete(0, tk.END)


# Get Username
username = input("Enter your username: ")

# GUI setup
root = tk.Tk()
root.title("Chat App")
root.geometry("400x500")

username_label = tk.Label(root, bg='blue', text=username, width=25, fg='white')
username_label.pack(pady=5, padx=10)

chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)
message_entry.bind("<Return>", lambda event: send_message())  # Send message on Enter key

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Receive messages from server
threading.Thread(target=receive_messages, daemon=True).start()

root.mainloop()
client.close()
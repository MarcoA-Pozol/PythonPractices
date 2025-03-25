from . client import receive_message
import threading
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# GUI for the Notifications System.
root = tk.Tk()

root.title("Notifications System")
root.geometry("400x500+100+50")

notifications_list = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD).pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# GUI Functions
def receive_notifications():
    """
        Receive notifications from the client.

        Attributes:
        - None

        Returns:
        - None
    """
    notification = receive_message()
    if notification:
        notifications_list.config(state=tk.NORMAL)
        
        notifications_list.insert(tk.END, f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  ---->  {notification}")

        notifications_list.config(state=tk.DISABLED)
        notification.yview(tk.END)

# Start receiving notifications.
threading.Thread(target=receive_notifications, daemon=True).start()

root.mainloop()

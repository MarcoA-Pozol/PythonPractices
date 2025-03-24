import socket
import threading

# Creating the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8600))

def receive_message():
    """
        Continuously receive messages from the server(server is deliverying messages steming from another user/client socket)
    """
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            print(msg)
        except ConnectionResetError:
            print('Disconnected from server.')
            break
            
# Obtaining username to identify the message sender
username = input('Enter your username:')

# Continuously receive messages from the server in a separe thread
threading.Thread(target=receive_message, daemon=True).start()

# Send message
while True:
    msg = input(f'You:')
    client.send(f'{username}: {msg}'.encode('utf-8'))
    
    # If message is empty, close the server
    if not msg:
        break

# Closing socket connection once the user decided to quit
client.close()
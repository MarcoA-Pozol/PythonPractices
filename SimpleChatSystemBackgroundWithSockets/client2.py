import socket
import threading

# Creating the client socket
client = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
client.connect('localhost', 8600)

def receive_message():
    """
        Continuously receive messages from the server(server is deliverying messages steming from another user/client socket)
    """
    while true:
        try:
            msg = client.recv(1024).decode('utf-8')
            print(msg)
        except ConnectionResetError:
            print('Disconnected from server.')
            break
            
# Obtaining username to identify the message sender
username = input('Enter your username:')

# Send message
while true:
    msg = input(f'You: '.encode('utf-8'))
    client.send(f'{username}: {msg}')
    
    # If message is empty, close the server
    if not msg:
        break

# Closing socket connection once the user decided to quit
client.close()
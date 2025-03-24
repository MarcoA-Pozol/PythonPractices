import socket
import threading

# Client socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8500))

def receive_message() -> str | None:
    """
        Receive messages from server if there are messages waiting to be delivered to a client.

        Attributes:
            None
        
        Returns:
            message(str): The message received from the server.
    """
    while True:
        try:
            message= client.recv(1024).decode('utf-8')
            return message
        except ConnectionError:
            raise ConnectionError
            

# Dict of users on the simulated database.
USERS_DICT = {
    'user1':{'username':'JohnPhillips', 'email':'johnphillips@gamil.com', 'password':'123password'},
    'user2':{'username':'LilianaHudson', 'email':'lilianahudson@gmail.com', 'password':'123password'},
    'user3':{'username':'AlbertFrank', 'email':'albertfrank@gmail.com', 'password':'123password'},
    'user4':{'username':'HannaGarcia', 'email':'hannagarcia@gmail.com', 'password':'123password'},
}

# Thread to execute the function that receives messages from the server and sends these to the client in a continuously manner.
threading.Thread(target=receive_message, daemon=True).start()

def send_message(user:object) -> None:
    """
        Send messages from client to server to a destination user.
        
        Attributes:
        - user(object): The destination user who will receive the sent message.

        Returns:
        - None
    """
    while True:
        # Send the message.
        message = input(f'Message:')
        client.send(f'{user}: {message}'.encode('utf-8'))

        # Close the server.
        if message == '\q':
            break

    # Close client connection.
    client.close()
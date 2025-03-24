import socket 
import threading
import logging

# Logging configuration.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Server Socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8500))
server.listen(6) # This server accepts 6 client connections.

# List of connected clients.
clients = []

def handle_client(client, addr):
    """
        Handle client's messages and connection.

        Attributes:
        - client: The client socket.
        - addr: The client address.

        Returns:
        - None.
    """
    logging.info(f'Client {addr} connected!')

    while True:
        try:
            # Receive and decode message from the client.
            message = client.recv(1024).decode('utf-8')

            # Close the server if client sent a '\q' request for server to close.
            if message == '\q':
                break

            logging.info(message)

            # Send message to Notification's client.
            clients[0].send(message.encode('utf-8'))

        except ConnectionResetError as ce:
            logging.error(msg=f'Impossible to handle the client message: {ce}')
            break

    logging.warning(f'Client {addr} disconnected.')
    clients.remove(client)
    client.close()

while len(clients) < 6:
    client, addr = server.accept()
    clients.append(client)
    threading.Thread(target=handle_client, args=(client, addr)).start()
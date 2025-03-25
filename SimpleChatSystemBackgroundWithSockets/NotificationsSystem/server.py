import socket 
import threading
import logging
from . notifications_client import notifications_client

# Logging configuration.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Server Socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8500))
server.listen(6) # This server accepts 6 client connections.

# List of connected clients.
clients = [notifications_client]

def handle_clients(client, addr):
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
            # Receive and decode messages from notifications client.
            message = clients[0].recv(1024).decode('utf-8')

            # Close the server if client sent a '\q' request for server to close.
            if message == '\q':
                break

            logging.info(message)

            # Send message to Notification's client.
            clients[1].send(message.encode('utf-8'))

        except ConnectionResetError as ce:
            logging.error(msg=f'Impossible to handle the client message: {ce}')
            break

    logging.warning(f'Client {addr} disconnected.')
    clients.remove(client)
    client.close()

async def check_for_server_connections_availability(clients:list=clients) -> None:
    """
        Checks up server is available to receive more client connections, if not, then it just pass up without receiving the client that requested to connect.

        Attributes:
        - clients(list): The list of clients connected to the server(it only accept 6 connections, the first one is for the client that manages the notifications and send them to other destination clients).

        Returns:
        - None
    """
    while len(clients) < 6:
        client, addr = server.accept()
        clients.append(client)
        threading.Thread(target=handle_clients, args=(client, addr)).start()
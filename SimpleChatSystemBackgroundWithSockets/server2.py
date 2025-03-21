import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8600))
server.listen(2) # Two connections / clients

clients = [] # Connected clients (users)

def handle_client(client, addr):
    """
        Handle messages and connection from a specific client.
    """
    print(f'Client {client} connected!')
    
    while True:
        try:
            msg = client.recv(1024).decode('utf-8') # Receive message from any client using the method
            
            if not msg:
                break # If message is empty, client is disconnected
                
            print(f'Message from {addr}: {msg}')
            
            # Send message to the other client
            for c in clients:
                if c != client:
                    c.send(msg.encode('utf-8')) # Don´t send the message back to the sender. Send to the client who is not sending the message (receiver).
        except ConnectionResetError:
            break # Handle client disconnection
    
    print(f'Client {addr} disconnected.')
    clients.remove(client)
    client.close()
    
# Accept only two clients
while len(clients) < 3:
    client, addr = server.accept() # Server will accept another client to connect while there are less than 2 clients in clients list
    clients.append(client)
    threading.Thread(target=handle_client, args=(client, addr)).start()
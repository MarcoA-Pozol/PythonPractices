import socket

# Server socket bint to "localhost" url in port 9999 using AF_INET and SOCK_STREAM
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen() # Set the Server socket to hear

client, addr = server.accept() # Accepting the client to connect to this server in the same channel

done = False

while not done:
    msg = client.recv(1024).decode('utf-8') # Message is what the client socket will sent from port 1024 in utf-8 decoded format
    if msg == 'quit':
        done = True
    else:
        print(msg)
    client.send(input('Message': ).encode('utf-8')) # Messages obtained from what the client sends as message decoded in utf-8

client.close()
server.close()
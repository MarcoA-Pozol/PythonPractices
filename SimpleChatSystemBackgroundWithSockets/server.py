import socket

# Server socket definition
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8600)) # use "socket.gethostname()" to make it vissible worldwide
server.listen(5) # Server with 5 connection request. Make this socker to be a server

print("Server´s waiting for connection...")

client, addr = server.accept() # Accepting the client to connect to server

print(f"Server´s connected to client: {addr}")

done = False

while not done:
    # Server sends first
    msg = input("Server: ")
    client.send(msg.encode('utf-8')) 

    if msg.lower() == 'quit':
        done = True
        break
    
    # Server waits for client response
    msg = client.recv(1024).decode('utf-8')
    print(f"Client: {msg}")
    
    # If client wants to quit
    if msg.lower() == "quit":
        done = True
        break

client.close()
server.close()
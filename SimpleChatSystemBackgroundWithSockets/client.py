import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8600))

done = False

while not done:
    # Client waits for server's message first
    msg = client.recv(1024).decode('utf-8')
    print(f"Server: {msg}")

    # If server wants to quit
    if msg.lower() == "quit":
        done = True
        break

    # Client sends response
    msg = input("Client: ")  
    client.send(msg.encode('utf-8'))

    # If client wants to quit
    if msg.lower() == "quit":
        done = True
        break

client.close()
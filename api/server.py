import socket
import threading

# 64 bytes - that's how much the server will receive.
HEADER = 64
FORMAT ='utf-8'
DISCONNECT_MESSAGE = 'DISCONNECTED!'
#choosing the port that the server runs on
PORT = 5050

# choosing the device that acting as server (ipv4 address)
# we can also go on cmd and type ipconfig
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

#what kind of socket do we want to create?
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#we need to bind our socket to the server
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')
    connected = True

    while connected:
        #this is blocking line because it won't move forward until we receive the message from the client. We need to specify how many bytes to receive.
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        #this is where we receive the message, the previous one is all about the length.
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f'{addr} {msg}')
        conn.send('Msg Received'.encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f'[SERVER] Server starts listening on {server}')
    while True:
        #this is blocking line because it won't move forward if we don't have a connection
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')

print(f'[SERVER] Server is starting...')
start()
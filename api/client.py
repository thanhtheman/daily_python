import socket

HEADER = 64
FORMAT ='utf-8'
DISCONNECT_MESSAGE = 'DISCONNECTED!'
PORT = 5050
SERVER = '192.168.2.14'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode())

send('Hello World')
send('Thanh is a talented software developer')
send('Thanh will get a backend dev job soon')
send(DISCONNECT_MESSAGE)


import socket
import threading

#choosing the port that the server runs on
PORT ='5050'

# choosing the device that acting as server (ipv4 address)
# we can also go on cmd and type ipconfig
SERVER = socket.gethostbyname(socket.gethostname())
ADDR= (SERVER, PORT)

#what kind of socket do we want to create?
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#we need to bind our socket to the server
server.bind(ADDR)
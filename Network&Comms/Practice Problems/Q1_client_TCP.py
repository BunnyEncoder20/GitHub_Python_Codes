import socket  # Get string length from server (TCP)
import time

sockc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[Client]client side socket created.")
time.sleep(1)

server_add = ('localhost', 9999)
sockc.connect(server_add)  # 1
print("[Client]connecting to server...")
time.sleep(1)
print(sockc.recv(1024).decode())  # 2

time.sleep(0.5)
msg = input("[Client]Enter data string: ")
sockc.send(str(msg).encode())  # 3
time.sleep(0.5)

print(sockc.recv(1024).decode())  # 4

sockc.close()
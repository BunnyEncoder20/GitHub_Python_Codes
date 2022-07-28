import socket  # Get string length from server (UDP)
import time

sockc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("[Client]client side socket created.")
time.sleep(1)

server_add = ('localhost', 9999)
sockc.sendto("Weebs saving the world".encode(),server_add) #1
msg,serverside=sockc.recvfrom (1024)  #2
print(msg.decode())

time.sleep(0.5)
data = input("[Client]Enter data string: ")
sockc.sendto(str(data).encode(),server_add)  #3

result,serverside=sockc.recvfrom(1024)
print(result.decode())  # 4

sockc.close()
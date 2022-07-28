import socket               #even parity checker client
from sys import modules
sockc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def parity_encoder(code):
    count = 0
    for i in code :
        if i=="1":
            count+=1
    #print("count : ",count)
    if (count%2)==0:
        return code+str(0)
    else:
        return code+str(1)

server_add=('localhost',9999)
sockc.connect(server_add)
print("[Client]client socket created")
print("[Client]connecting to server...")

print(sockc.recv(1024).decode()) #1
print("[Client]Enter the code in bianry :")
code = input()
encoded = parity_encoder(code)

print("[Client]code :    ",code)
print("[Client]encoded : ",encoded)

sockc.send(encoded.encode())  #2
print("[Client]sending code...")

print(sockc.recv(1024).decode())   #3
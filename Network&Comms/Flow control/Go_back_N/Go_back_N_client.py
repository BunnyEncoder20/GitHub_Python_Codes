import socket 
import time 
import sys 
import random

sockc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_add=('localhost',9999)


print("[Client]Welcome to GBN-ARQ chatroom")
name = input("[Client]Enter your name : ")
print("\n[Client]connecting to server...")
sockc.connect(server_add)
time.sleep(1)
print("[Client]connected!")

sockc.send(name.encode())
server_name = sockc.recv(1024).decode()
print("[Client]",server_name," has joined the chatroom")
print("[Client]Enter [e] to exit chatroom\n")

while True:
    msg = sockc.recv(1024).decode()
    k = sockc.recv(1024).decode()
    k = int(k)
    i=0
    a=""
    b=""
    message=""
    # f=random.randint(0,1)

    while i!=k:
        f=0 #f=random.randint(0,1) - takes too long
        if(f==1):
            b="ACK lost"
            message=sockc.recv(1024).decode()
            sockc.send(b.encode())

        elif(f==0):
            b="Acknowledged "+str(i)
            message=sockc.recv(1024).decode()
            sockc.send(b.encode())
            a=a+message
            i+=1

    print("[Client]Message : ",msg)
#fat
import socket 
import time 
import sys 
import random
from datetime import datetime

sockc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_add=('localhost',9999)

def rnow():
    now = datetime.now()
    return str(now.strftime("%H:%M:%S"))
    

print("[Client]Welcome to GBN-ARQ chatroom")
name = input("[Client]Enter your name : ")
print("\n[Client]connecting to server...")
sockc.connect(server_add)#1
time.sleep(1)
print("[Client]connected!")

sockc.send(name.encode())#2
server_name = sockc.recv(1024).decode()#3
print("[Client]",server_name," has joined the chatroom")
print("[Client]Enter [e] to exit chatroom\n")

while True:
    msg = sockc.recv(1024).decode()#4
    k = sockc.recv(1024).decode()#5
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
            message=sockc.recv(1024).decode()#6
            sockc.send(b.encode())#7

        elif(f==0):
            b="Acknowledged "+str(i)+" at "+rnow()
            message=sockc.recv(1024).decode()#8
            sockc.send((b+"\nlength : "+str(len(message))).encode())#9
            a=a+message
            i+=1

    print("[Client]Message : ",msg)
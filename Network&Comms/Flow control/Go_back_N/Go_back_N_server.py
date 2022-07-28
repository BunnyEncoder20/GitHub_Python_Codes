import socket 
import time 
import sys 
import random

def binary_convertor(n):
    return n.replace("0b","")

def binarycode(s):
    a_byte_array = bytearray(s, "utf8")

    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(binary_convertor(binary_representation))

    #print(byte_list)
    a=""
    for i in byte_list:
        a=a+i
    return a

print("[Server]Server chatroom is booting up...")
time.sleep(1)
socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_add=('localhost',9999)
socks.bind(server_add)
name = "GBN-Server"
print("[Server]Server Name is : ",name)
socks.listen(1)
print("[Server]Waiting for connections...")

connection,client_add=socks.accept()
print("[Server]received connection from : ",client_add)

client_name = connection.recv(1024).decode()
print("[Server]",client_name," has joined the chatroom")
print("[Server]Enter [e] to exit the chat room")
connection.send(name.encode())

while True:
    message=input(str("Me : "))
    connection.send(message.encode())
    if message == "[e]" :
        message = "Left the chatroom!"
        connection.send(message.encode())
        print("\n")
        break
    message=binarycode(message)
    f=str(len(message))
    connection.send(f.encode())

    i=0;
    j=int(input("Enter the window size : "))
    b=""
    j-=1
    f=int(f)
    k=j

    while i!=f:
        while(i!=(f-j)):
            connection.send(message[i].encode())
            b=connection.recv(1024).decode()
            print(b)

            if(b!="ACK lost"):
                time.sleep(1)
                print("ACK recieved! \nSliding window range : "+str(i+1)+" to "+str(k+1))
                print("Now sending the next packet")
                i+=1
                k+=1
                time.sleep(1)
            else:
                time.sleep(3)
                print("ACK of the data lost!\nSliding window range : "+str(i+1)+" to "+str(k+1))
                print("Now resending the same packet")
                time.sleep(1)
        
        while(i!=f):
            connection.send(message[i].encode())
            b=connection.recv(1024).decode()
            print(b)

            if(b!="ACK lost"):
                time.sleep(1)
                print("ACK received!\nSliding window range : "+str(i+1)+" to "+str(k))
                print("Now sending the next packet")
                i=i+1
                time.sleep(1)
            else:
                time.sleep(3)
                print("ACK of the data lost!\nSliding window range "+str(i+1)+" to "+str(k))
                print("Now Resending the same packet")
                time.sleep(1)


import socket 
import random

socks= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_add=('localhost',9999)
socks.bind(server_add)
socks.listen(1)

print("[Server]server booting up...")
print("[Server]server socket created")
print("[Server]server binded to port")
print("[Server]waiting for client to send messages\n")

N = 4
w_start = 0
w_end = w_start + N-1
recving = []
new = 1

connection,add = socks.accept()     #connecting to the client side
print("Connected to ",str(add))

while True:
    data = connection.recv(1024).decode()
    recv = int(data)
    limit = recv+N-1
    count,flag=0,0
    ack = recv

    rand = random.randint(1,4)
    if new == 1:        #recved new frame of new window
        while(count!=rand):
            temp = random.randint(recv,limit)

            if temp not in recving:
                print("[Server]recieved frame : ",temp)
                count+=1
                flag=1
                recving.append(temp)
    else:
        print("[Server]recieved frame : ",recv)         #recved new frame of old window
        recving.append(recv)
        flag = 1
    
    if flag==1 :
        for i in range(recv,limit+1):
            if i not in recving:
                ack=i
                break
            ack = i+1
    print("[Server]sending ACK : ",ack)  #next expected frame

    connection.send(str(ack).encode())      #sending ack to client

    if ack>w_end:
        w_start = ack;
        w_end = w_start+N-1
        new = 1         #will recv a new frame of new window
    else :
        new = 0         #will recv a new frame of old window
connection.close()
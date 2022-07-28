import socket

sockc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_add=('localhost',9999)
sockc.connect(server_add)
# socket.timeout(0.5)

N = 4
w_start = 0
w_end = w_start + N-1
sending = []
flag=0

client = input("[Client]Press any key to start sending frames : ")
while client.lower().strip()!="close" :
    print("[Client]sending frames...")
    if flag == 0 :
        for i in range(N):
            sending.append(w_start+i)
        for i in sending :
            print("Frame - ",i)
    else:
        print("Frame - ",w_start)
    
    msg=str(w_start)
    sockc.send(msg.encode())    #1 sending frame
    data = sockc.recv(1024).decode()
    msg=str(data)
    ack = int(msg)

    if ack not in sending:
        w_start = ack
        w_end = w_start+N-1
        flag = 0        #when window slides forward, send new frame
        for i in range(N):
            sending.pop()   #empty the sending window
        else:
            w_start = ack
            flag = 1    # resend old frame
    
    print("\n[Client]received from server : "+data)
    client = input("[Client]Press any key to start sending frames : ")

sockc.close()
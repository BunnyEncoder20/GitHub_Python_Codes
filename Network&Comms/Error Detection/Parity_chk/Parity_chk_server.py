import socket                       #even parity checker server
socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("[Server]server booting up...")
print("[Server]server socket created")

def even_parity(code):
    count=0
    for i in code:
        if i==1:
            count+=1
    if (count%2)==0:
        print("[Server]Message was correct")
        return True
    else:
        print("[Server]Message has error")
        return False

server_add = ('localhost',9999)
socks.bind(server_add)
socks.listen(3)
print("[Server]server binded")
print("[Server]waiting for client to connect")
print("\n")

while(True):
    connection,address=socks.accept()
    print("[Server]connected with client : ",address)
    connection.send("[Server]connected to parity_chk server".encode()) #1
    code = connection.recv(1024).decode()   #2
    print("[Server]code recieved : ", code)

    if even_parity(code):
        connection.send("[Server]The message has no errors!".encode())      #3
    else:
        connection.send("[Server]There was a error in the message!".encode()) #3
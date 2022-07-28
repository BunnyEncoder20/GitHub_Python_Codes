import socket
import time

socks=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("[Server]server side socket created.")
time.sleep(1)

server_add = ('localhost',9999)
socks.bind(server_add)
socks.listen(3)
print("[Server]server binded to port")
time.sleep(0.3)
print("[Server]waiting for clients to connect...\n")

while (True):
    connection,client_add=socks.accept()        #1
    print("[Server]server connected to client :\n",client_add)
    connection.send("[Server]Connected to String_Length server!\n".encode())        #2

    recv_data=connection.recv(1024).decode()        #3
    l=str(len(recv_data))
    print("[Server]Recieved Data = "+recv_data)
    print("[Server]Data Length = "+l)
    connection.send(("[Server]String's Length is = "+l).encode())       #4
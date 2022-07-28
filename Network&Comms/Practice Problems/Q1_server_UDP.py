import socket       # Get string length from server (UDP)
import time

socks=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("[Server]server side socket created.")
time.sleep(0.5)

server_add = ('localhost',9999)
socks.bind(server_add)
print("[Server]server binded.")
time.sleep(0.5)
print("[Server]waiting for clients to connect...")

while (True):
    data,client_add=socks.recvfrom(1024)        #1
    print("[Server]server connected to client :",client_add)
    print("Client side message :\n"+data.decode())
    socks.sendto("[Server]Connected to String_Length server!\n".encode(),client_add)        #2

    recv_data,clientside=socks.recvfrom(1024)        #3
    l=str(len(recv_data.decode()))
    print("[Server]Recieved Data = "+str(recv_data.decode()))
    print("[Server]Data Length = "+l)
    socks.sendto(("[Server]String's Length is = "+l).encode(),client_add)       #4
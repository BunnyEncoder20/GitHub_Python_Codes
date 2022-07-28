import socket       #Capitalization UDP server

socks=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("[server]Server socket created")

server_addr=('localhost',9999)
socks.bind(server_addr)
print("[server]Waiting for client to connet...")

while True:
    data,addr=socks.recvfrom(1024)  #1
    data=str(data.decode("utf-8")).upper()
    #data=data.upper()
    print("[Server]Connected to client : ",addr)
    print("[Server]Recieved word from client")

    socks.sendto(data.encode("utf-8"),addr) #2



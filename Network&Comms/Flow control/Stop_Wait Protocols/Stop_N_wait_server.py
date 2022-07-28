import socket

socks = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_add=('localhost',9999)
socks.bind(server_add)
ackwonledgement = "[Server]message received."
print("[Server]server booting up...")
print("[Server]server binded to port")
print("[Server]waiting for client to send messages\n")

while True:
    message,client_add= socks.recvfrom(1024)
    print("[Server]connected to : ",client_add)
    print("[Server]received : "+message.decode("utf-8"))
    print("[Server]acknowledgement sent")
    socks.sendto(ackwonledgement.encode("utf-8"),client_add)

import socket           #Echo ServerSide UDP

socks = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('[server]Sock socket was created !')

server_addr=('localhost',9999)
socks.bind(server_addr)
print('[server]Waiting for client connection....\n')

while True:
    sentence,address= socks.recvfrom(1024)   #1
    sentence=str(sentence.decode("utf-8"))
    print('[server]Connected with Client Address : ',address)
    #print('\n\n')
    #sentence,address=socks.recvfrom(1024).decode()
    print('[server]Recieved : ',sentence)
    socks.sendto(sentence.encode("utf8"),address) #2
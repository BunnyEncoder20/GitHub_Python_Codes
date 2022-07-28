import socket           #Caps ServerSide

socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Sock socket was created for server!\n\n')

server_addr=('localhost',9999)
socks.bind(server_addr)

socks.listen(3)
print('Waiting for client connection....\n')

while True:
    Connection,address= socks.accept()
    print('Connected !\nWith Client Address : ',address)
    print('\n\n')
    sentence=Connection.recv(1000).decode()
    if sentence=='\0':
        break
    print('Recieved : ',sentence)
    caps=sentence.upper()
    Connection.sendall(caps.encode())



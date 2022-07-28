import socket           #Echo ServerSide

socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Sock socket was created !\n\n')

server_addr=('localhost',9999)
socks.bind(server_addr)

socks.listen(3)
print('Waiting for client connection....\n')

client,address= socks.accept()
print('Connected !\nWith Client Address : ',address)
print('\n\n')
sentance=client.recv(1000).decode()
print('Recieved : ',sentance)
client.sendall(sentance.encode())
client.close()
socks.close()


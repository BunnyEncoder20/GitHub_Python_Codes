import socket       #Echo Client side

sockc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('[client]Socket created for client')

server_addr=('localhost',9999)
sockc.connect(server_addr) 

message = input('Input sentence :')
print('Sending : ',message)
sockc.sendall(message.encode())
print("\nOriginal : ",message)
echo=sockc.recv(1000).decode() 
print('Capitals : ',echo)
print('\n')
sockc.close() 
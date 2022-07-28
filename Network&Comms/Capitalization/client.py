import socket       #Caps Client side

sockc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created for client')

server_addr=('localhost',9999)
sockc.connect(server_addr)

message = input('Input sentence :')
print('Sending : ',message)
sockc.sendall(message.encode())
print("\nOriginal : ",message)
caps=sockc.recv(1000).decode() 
print('Capitals : ',caps)

sockc.close() 
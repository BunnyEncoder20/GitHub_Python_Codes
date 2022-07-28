import socket  #palindrome client side

sockc= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created for client side')

server_address=('localhost',9999)
sockc.connect(server_address)


print(sockc.recv(1024).decode())
string=input('[client]Enter the string : ')
sockc.sendall(string.encode())
print('[client]Sending...')
print(sockc.recv(1024).decode())
print(sockc.recv(1024).decode())
print('\n')
import socket

c=socket.socket()

c.connect(('localhost',9999))  #IP_address of the server and port nuymber to connect with
print('\n\n')
#2 step
print(c.recv(1024).decode()) #decoding the recieved data from bytes format to string

name = input('Enter your name : ')
#3 step
c.send(bytes(name,'utf-8'))
#6 step
message = c.recv(1024).decode()
print('\n',message)
import socket

s=socket.socket()       #creating a socket
print('Socket was created !\n');

s.bind(('localhost',9999)) #takes IP address & the port number
#binding the socket to a port

s.listen(3)     # waiting for client to join

print('Waiting for connections...\n')

while True:
    c,address = s.accept() #client socket and address

    #1 step
    c.send(bytes('You have connected with LocalBunny Server !\n','utf-8'))
    #4 step
    name = c.recv(1024).decode()
    print('Connected with :',name,address)
    print('\n')
    #5
    c.send(bytes('Welcome to the server !\n','utf-8'))
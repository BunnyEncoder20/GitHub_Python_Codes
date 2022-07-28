import socket #Palindrome serverside


def palindrome(string):     #function to check palindrome
    for i in (0,int(len(string)/2)):
        if string[i]!=string[len(string)-i-1]:
            return False
    return True
            

socks=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('[server]Socket created for server')

server_address=('localhost',9999) #socket binding important !
socks.bind(server_address)
print('[server]Socket binded')

socks.listen(3)
print('[server]Waiting for client to connect...')

while True:
    connection,address=socks.accept()
    print('\n[server]Connected with : ',address)
    #print('\n')
    connection.sendall('[server]Connected with Palindrome Server'.encode())
    string=connection.recv(1000).decode()
    print('[server]Recieved : ',string)
    #logics
    mes1='[server]Yes,it IS a palindrome'
    mes2='[server]No,it is NOT a palindrome'
    
    print('[server]Function called')
    if palindrome(string):
        print('[server]Returned True')
        connection.sendall(mes1.encode())
    else:
        print('[server]Returned False')
        connection.sendall(mes2.encode())


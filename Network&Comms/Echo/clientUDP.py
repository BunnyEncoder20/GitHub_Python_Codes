import socket       #Echo Client side UDP

sockc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('[client]Socket created for client')


server_add=('localhost',9999)
#sockc.connect(server_addr) 

message = input('[client]Input sentence :\n')
print('[client]Sending...')

sockc.sendto(message.encode("utf-8"),server_add)  #1

print("\n[client]Original : ",message)
echo,server=sockc.recvfrom(1024) #2
echo=echo.decode("utf-8")
print('Echo : Yes, ',echo)
print('\n')
sockc.close() 
# encoding string  str_enc= str.encode(encoding='utf8') 
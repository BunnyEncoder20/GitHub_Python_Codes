import socket       #CRC server
import time
key = "1001"

def XOR(a,b):
    result=[]
    for i in range(1,len(b)):
        if a[i]==b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def division(divident,divisor):
    pick = len(divisor)
    temp = divident[0:pick]
    
    while pick<len(divident):
        if temp[0]=='1':
            temp = XOR(divisor,temp) + divident[pick]
        else:
            temp = XOR('0'*pick,temp) + divident[pick]
        pick+=1 # moving forward
    if temp[0]=='1':
        temp = XOR(divisor, temp) 
    else: 
        temp = XOR('0'*pick, temp) 
   
    # chk = temp 
    return temp

def decode_data(data,key):
    l = len(key) 
    appended_data = data + '0'*(l-1) 
    remainder = division(appended_data, key) 
   
    return remainder

socks=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("[Server]server booting up...")
time.sleep(1)
print("[Server]server socket created")
time.sleep(0.5)
server_add=('localhost',9999)
socks.bind(server_add)
socks.listen(3)
print("[Server]server binded")
print("[Server]wating for clients to connect...\n")

while True:
    connection,client_add = socks.accept()
    print("[Server]connected to client : ",client_add)
    connection.send("[Server]Welcome to CRC server".encode())       #1

    data = connection.recv(1024).decode()       #2
    print("[Server]received data : ",data)
    remainder=decode_data(data,key)
    print("[Server]remainder after decoding : "+remainder)

    temp = "0" * (len(key) - 1)     #checking for any error
    if remainder == temp: 
        connection.send("[Server]your Data was recieved\n[Server]No error found".encode()) 
    else: 
        connection.send("Error in data recieved".encode()) 
  
    connection.close() 
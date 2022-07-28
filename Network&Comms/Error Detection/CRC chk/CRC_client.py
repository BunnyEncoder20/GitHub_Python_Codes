import socket    #CRC client
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

def encode_data(data,key):
    l = len(key) 
    appended_data = data + '0'*(l-1) 
    remainder = division(appended_data, key) 
   
    # Append remainder in the original data 
    code = data + remainder 
    return code 

sockc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_add=('localhost',9999)
print("[Client]connecting to server...")
time.sleep(1)
sockc.connect(server_add)
print(sockc.recv(1024).decode())        #1
time.sleep(1)

msg = input("\nEnter the data you want to send : ")
data =(''.join(format(ord(x), 'b') for x in msg)) 
print(data)

transmitted_data = encode_data(data,key)
print("[Client]Transmitted data : ",transmitted_data)
print("[Client]Transmitting the data...")
sockc.send(transmitted_data.encode())           #2
time.sleep(0.5)
print("[Client]Transmission completed")
time.sleep(2)

print(sockc.recv(1024).decode())        #3
sockc.close()
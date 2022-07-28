from random import randrange
import socket 
import time

def redundant_bits(l):
    for i in range(l):
        if(2**i>=l+i+1):
            return i

def position_redundant_bits(data,r):
    j,k,m=0,1,len(data)
    result=""
    for i in range(1,m+r+1):
        if(i==2**j):        #if power of 2 , then put 0
            result=result+'0'
            j+=1
        else:           #otherwise append the code
            result = result + data[-1*k]
            k+=1
    return result[::-1]

def parity_bits(arr,r):
    n=len(arr)
    for i in range(r):
        val = 0
        for j in range(1,n+1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr

sockc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_add=('localhost',9999)
print("[Client]client socket created")
print("[Client]connecting to Hamming server...")
time.sleep(1)
sockc.connect(server_add)
print(sockc.recv(1024).decode())        #1

time.sleep(1)
print("\n[Client]Enter the binary message : ")
msg1 = "101010011101"
time.sleep(1)
print("[Client]entered message : ",msg1)
l = len(msg1)
red = redundant_bits(l)     #redundant bits fetching
msg2 = position_redundant_bits(msg1,red)    #determine position of redundant bits
msg3 = parity_bits(msg2,red)

print("\n[Client]Sending message : "+msg3)
time.sleep(1)
sockc.send(msg3.encode())       #2
sockc.send(str(red).encode())       #3
print("[Client]sent!")

sockc.close()
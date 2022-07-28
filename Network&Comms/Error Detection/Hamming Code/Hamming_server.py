import socket       #Hamming Server
import time 

def detectError(arr, nr):
    n = len(arr)
    res = 0
 
    # Calculate parity bits again
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        res = res + val*(10**i)
 
    # Convert binary to decimal
    return int(str(res), 2)

socks=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("[Server]server booting up...")
time.sleep(1)
print("[Server]server socket created")
server_add=('localhost',9999)
socks.bind(server_add)
socks.listen(3)
print("[Server]server binded")
print("[Server]wating for clients to connect...\n")

while(True):
    connection,address=socks.accept()
    print("[Server]connected to client : ",address)
    connection.send("[Server]Welcome to Hamming Server!".encode())  #1

    data = connection.recv(1024).decode()   #2
    print("[Server]data recieved :   "+data)
    data = "11010100111110100" #error introduced at 5th position
    print("[Server]corruptied data : "+data)
    
    red = connection.recv(1024).decode()        #3
    detected_pos = detectError(data,int(red))
    print("[Server]the position of error is "+str(detected_pos))

    # data = 11010100111100100
import socket       #Palindrome server side UDP 

socks=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("[Server]Server side socket made")
server_addr=('localhost',9999)
socks.bind(server_addr)
print("[Server]Server side binded to port")
print("[Server]Waiting for client...\n")

def palindrome(string):     #function to check palindrome
    for i in (0,int(len(string)/2)):
        if string[i]!=string[len(string)-i-1]:
            return False
    return True

while True:
    word,addr=socks.recvfrom(1024)  #1
    word=word.decode("utf-8")
    print("[Server]Server recieved : ",word)
    print("[Server]Palindrome function called")

    if palindrome(word):
        print("[Server]Functioned returned True")   
        socks.sendto("[Server]The sent word IS a Palindrome!".encode("utf-8"),addr) #2
    else:
        print("[Server]Function returned False")
        socks.sendto("[Server]The sent word is NOT a Palindrome!".encode(),addr) #2

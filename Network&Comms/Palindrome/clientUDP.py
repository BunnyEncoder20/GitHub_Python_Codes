import socket       #Palindrome client side UDP 

sockc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("[Client]Client side socket created.")

server_addr=('localhost',9999)
word=input("[Client]Enter the word : ")
print("[Client]Sending...")

sockc.sendto(word.encode("utf-8"),server_addr)   #1

results,serverside=sockc.recvfrom(1024) #2
results=results.decode("utf-8")
print(results)
print("\n")

sockc.close()
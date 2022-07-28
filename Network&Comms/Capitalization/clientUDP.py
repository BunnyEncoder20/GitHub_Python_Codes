import socket   

sockc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("[client]Client socket created.")

server_addr=('localhost',9999)

message=input("\nEnter the sentence : ")
print("[Client]Sending to server...\n")
sockc.sendto(message.encode("utf-8"),server_addr)  #1

print("[Client]Original : ",message);
caps,serverside=sockc.recvfrom(1024) #2;
caps=caps.decode("utf-8")
print("[Client]Capitalized : ",caps)
print("\n")

sockc.close()
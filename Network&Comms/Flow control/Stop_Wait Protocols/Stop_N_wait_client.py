import socket

sockc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_add=('localhost',9999)
socket.timeout(0.1)
message = input("Enter the message : ")
ackwonledged = False

while True:
    sockc.sendto(message.encode("utf-8"),server_add)
    
    while not ackwonledged:
        try:
            ACK,address = sockc.recvfrom(1024)  #1
            ackwonledged = True     #exit the loop if ack recvied 
        except socket.timeout:
            sockc.sendto(message,server_add)    
            #send that frame again if the ack didn't come in time
    print(ACK.decode("utf-8"))
    message = input()

sockc.close()
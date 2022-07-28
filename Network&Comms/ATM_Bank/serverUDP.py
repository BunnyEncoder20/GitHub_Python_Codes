import socket

socks=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("[server]ATM Server socket created")

server_add=('localHost',9999)
socks.bind(server_add)
print("[server]ATM server binded to ",server_add)
print("[server]Waiting for client to connect...\n")

#making the accounts    
acc_number={1001:10002343,1002:10005899,1003:10009838,1004:10002389,1005:10003644}
acc_balance={1001:10000,1002:12000,1003:25000,1004:14500,1005:50000}
acc_name={1001:"Bunny Verma",1002:"Tarun Puneet",1003:"Soma Senpai",1004:"Bunnu Bio",1005:"Hooda Haryanvi"}

while True:
    call,add=socks.recvfrom(1024)#1
    socks.sendto("[server]Connected to HDFC Bank Server\nEnter your PIN :".encode("utf-8"),add) #2
    pin,clientside=socks.recvfrom(1024) #3
    pin=int(pin.decode("utf-8")) 
    print("[server]Receieved PIN : ",pin)
    
    if pin in acc_name.keys():  #check for the account
        socks.sendto(str(1).encode("utf-8"),add) #4
        socks.sendto("Account of client identified\n".encode("utf-8"),add) #5
        #temp1=socks.recv(1024) #

        socks.sendto(acc_name[pin].encode("utf-8"),add)  #5
        #temp2=socks.recv(1024) #

        socks.sendto(str(acc_number[pin]).encode("utf-8"),add)  #7
        #temp3=socks.recv(1024) #

        socks.sendto(str(acc_balance[pin]).encode("utf-8"),add)  #8

        choice,clientside=socks.recvfrom(1024)  #9
        choice=int(choice.decode("utf-8"))
        #print("[server]recieved choice : ",choice)

        if choice==1:
            #print("Account Balance is : ₹",int(sockc.recv(1024).decode()))
            socks.sendto(str(acc_balance[pin]).encode("utf-8"),add)         #10
            print("[server]Account balance sent for ",acc_number[pin])
        elif choice==2:
            #withdraw=input("Enter the withdraw amount : ")
            #print("Money withdraw successfull.\nNew Balance : ₹",int(sockc.recv(1024).decode()))
            m11,clientside=socks.recvfrom(1024)
            withdraw=int(m11.decode("utf-8"))    #11
            acc_balance[pin]-=withdraw
            socks.sendto(str(acc_balance[pin]).encode("utf-8"),add)     #12
            print("[server]Account balance modified for :",acc_number[pin],"\n[server]Amount withdrawn : ",withdraw,"\n[server]Balance : ",acc_balance[pin])
        elif choice==3:
            #deposite=input("Enter the deposite amount : ")
            #print("Money deposite successful.\nNew balance : ₹",int(sockc.recv(1024).decode()))
            m13,clientside=socks.recvfrom(1024)
            deposite=int(m13.decode("utf-8"))    #13
            acc_balance[pin]+=deposite
            socks.sendto(str(acc_balance[pin]).encode("utf-8"),add)     #14
            print("[server]Account balance modified for :",acc_number[pin],"\n[server]Amount deposited : ",deposite,"\n[server]Balance : ",acc_balance[pin])
        else:
            print("[server]Invalid choice aborting")
    else:
        socks.sendto(str(0).encode("utf-8"),add) #4
        socks.sendto("[server]Invalid PIN aborting...".encode("utf-8"),add) #14
        print("[server]Invalid PIN aborted connection")
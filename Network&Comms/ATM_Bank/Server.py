import socket

socks=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("[server]ATM Server socket created")

server_add=('localHost',9999)
socks.bind(server_add)
print("[server]ATM server binded")

socks.listen(3)
print("[server]Waiting for client to connect...\n")

#making the accounts    
acc_number={1001:10002343,1002:10005899,1003:10009838,1004:10002389,1005:10003644}
acc_balance={1001:10000,1002:12000,1003:25000,1004:14500,1005:50000}
acc_name={1001:"Bunny Verma",1002:"Tarun Puneet",1003:"Soma Senpai",1004:"Bunnu Bio",1005:"Hooda Haryanvi"}

while True:
    connection,client_add=socks.accept()
    print("\n[server]Connected with client")
    connection.send("[server]Connected to HDFC Bank Server\nEnter your PIN :".encode()) #1
    pin=int(connection.recv(1024).decode()) #2 pin verification request

    if pin in acc_name.keys():  #check for the account
        connection.send("Account of client identified\n".encode()) #3
        temp1=connection.recv(1024) #4

        connection.send(acc_name[pin].encode())  #5
        temp2=connection.recv(1024) #6

        connection.send(str(acc_number[pin]).encode())  #7
        temp3=connection.recv(1024) #temp3request

        connection.send(str(acc_balance[pin]).encode())  #temp3reply

        choice=int(connection.recv(1024).decode())  #8
        #print("[server]recieved choice : ",choice)

        if choice==1:
            #print("Account Balance is : ₹",int(sockc.recv(1024).decode()))
            connection.send(str(acc_balance[pin]).encode())     #9
            print("[server]Account balance sent for ",acc_number[pin])
        elif choice==2:
            #withdraw=input("Enter the withdraw amount : ")
            #print("Money withdraw successfull.\nNew Balance : ₹",int(sockc.recv(1024).decode()))
            withdraw=int(connection.recv(1024).decode())    #10
            acc_balance[pin]-=withdraw
            connection.send(str(acc_balance[pin]).encode())     #11
            print("[server]Account balance modified for :",acc_number[pin],"\n[server]Amount withdrawn : ",withdraw,"\n[server]Balance : ",acc_balance[pin])
        elif choice==3:
            #deposite=input("Enter the deposite amount : ")
            #print("Money deposite successful.\nNew balance : ₹",int(sockc.recv(1024).decode()))
            deposite=int(connection.recv(1024).decode())    #12
            acc_balance[pin]+=deposite
            connection.send(str(acc_balance[pin]).encode())     #13
            print("[server]Account balance modified for :",acc_number[pin],"\n[server]Amount deposited : ",deposite,"\n[server]Balance : ",acc_balance[pin])
        else:
            print("[server]Invalid choice aborting")
    else:
        connection.send("[server]Invalid PIN aborting...".encode()) #14
        print("[server]Invalid PIN aborted")
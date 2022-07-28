import socket
acc_number={1001:10002343,1002:10005899,1003:10009838,1004:10002389,1005:10003644}

sockc= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_add=('localhost',9999)
sockc.connect(server_add)

print(sockc.recv(1024).decode())    #1
pin=input()
sockc.send(str(pin).encode())       #2 sending pin for verification


if int(pin) in acc_number.keys():
    #print("here")
    print(sockc.recv(1024).decode())    #3
    sockc.send("temp1".encode())        #4
    print("Account Holder Name :",sockc.recv(1024).decode())    #5
    sockc.send("temp2".encode())    #6
    print("Account Number      :",int(sockc.recv(1024).decode()))    #7
    sockc.send("temp3".encode())    #temp3
    print("Available Balance   : \n₹ ",int(sockc.recv(1024).decode()))    #temp3recv

    print("\n***ATM Menu***\n1.Account Balance\n2.Withdraw\n3.Deposite")
    choice=int(input("Enter choice : "))
    sockc.send(str(choice).encode())    #8
    print("\n")


    if choice==1:
        print("[server]Account Balance is : ₹",int(sockc.recv(1024).decode()))  #9
    elif choice==2:
        withdraw=input("Enter the withdraw amount : ")
        sockc.send(str(withdraw).encode())      #10
        print("Money withdraw successfull.\nNew Balance : ₹",int(sockc.recv(1024).decode()))        #11
    elif choice==3:
        deposite=input("Enter the deposite amount : ")
        sockc.send(str(deposite).encode())      #12
        print("Money deposite successful.\nNew balance : ₹",int(sockc.recv(1024).decode()))     #13
    else:
        print("Invalid choice aborting")
else:
    #print("not there")
    print(sockc.recv(1024).decode())        #14

print("End of Process")
sockc.close()
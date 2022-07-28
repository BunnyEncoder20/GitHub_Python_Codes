import socket
#acc_number={1001:10002343,1002:10005899,1003:10009838,1004:10002389,1005:10003644}

sockc= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_add=('localhost',9999)


sockc.sendto("connect to server".encode("utf-8"),server_add) #1
m1,serverside=sockc.recvfrom(1024)      #2
print(m1.decode("utf-8"))    
pin=input()
sockc.sendto(str(pin).encode("utf-8"),server_add)       #3 sending pin for verification

chk,serverside=sockc.recvfrom(1024) #4
chk=int(chk.decode("utf-8"))
if chk==1:                  #if PIN is there in the list of the server
    #print("here")
    m5,serverside=sockc.recvfrom(1024)     #5
    print(m5.decode("utf-8"))
    m6,serverside=sockc.recvfrom(1024)  #6
    m7,serverside=sockc.recvfrom(1024)     #7
    m8,serverside=sockc.recvfrom(1024)      #8
    print("Account Holder Name :",m6.decode("utf-8"))    
    print("Account Number      :",int(m7.decode("utf-8")))    
    print("Available Balance   : ₹ ",int(m8.decode("utf-8")))    

    print("\n***ATM Menu***\n1.Account Balance\n2.Withdraw\n3.Deposite")
    choice=int(input("Enter choice : "))
    sockc.sendto(str(choice).encode("utf-8"),server_add)    #9
    print("\n")


    if choice==1:
        m10,serverside=sockc.recvfrom(1024)
        print("[server]Account Balance is : ₹",int(m10.decode("utf-8")))  #10
    elif choice==2:
        withdraw=input("Enter the withdraw amount : ")
        sockc.sendto(str(withdraw).encode("utf-8"),server_add)      #11
        m12,serverside=sockc.recvfrom(1024)
        print("Money withdraw successfull.\nNew Balance : ₹",int(m12.decode("utf-8")))        #12
    elif choice==3:
        deposite=input("Enter the deposite amount : ")
        sockc.sendto(str(deposite).encode("utf-8"),server_add)      #13
        m14,serverside=sockc.recvfrom(1024)
        print("Money deposite successful.\nNew balance : ₹",int(m14.decode("utf-8")))     #14
    else:
        print("Invalid choice aborting")
else:
    #print("not there")
    m14,serverside=sockc.recvfrom(1024)
    print(m14.decode("utf-8"))        #14
    
sockc.close()
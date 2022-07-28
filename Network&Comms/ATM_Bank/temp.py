acc_number={1001:10002343,1002:10005899,1003:10009838,1004:10002389,1005:10003644}
acc_balance={1001:1000,1002:1200,1003:2500,1004:1450,1005:5000}

while True:
    connection,client_add=socks.accept()
    print("[server]Connected with client : ",client_add)
    connection.sendall("[server]Connected to HDFC Bank Server\nEnter your PIN :".encode())
    pin=int(connection.recv(1024).decode())
    print("[server]Server recieved pin : ",pin)

    print(acc_number.keys())

    if pin in acc_balance.keys():
        print("yes done")
        connection.send('[server]Account Number : '.encode())
        connection.send(str(acc_number[pin]).encode())
        connection.send('\n\n[server]Account Balance : \n'.encode())
        connection.send(str(acc_balance[pin]).encode())
    else:
        print("Invalid pin entered")
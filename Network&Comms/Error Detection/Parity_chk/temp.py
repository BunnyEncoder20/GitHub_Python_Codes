def parity_encoder(s):
    count = 0
    for i in s :
        if i == "1" :
            count+=1
    print("count : ",count)
    if (count%2)==0:
        return s+"0"
    else:
        return s+"1"

print("[Client]Enter the code in bianry :")
code = input()
encoded = parity_encoder(code)
print("Encoded : ",encoded)
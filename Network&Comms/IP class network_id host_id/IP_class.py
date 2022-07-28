def getclass(ip):       #get the class of IP
    if 0<=ip[0] and ip[0]<=127:
        return "A"
    elif 128<=ip[0] and ip[0]<=191:
        return "B"
    elif 192<=ip[0] and ip[0]<=223:
        return "C"
    elif 224<=ip[0] and ip[0]<=239:
        return "D"
    else:
        return "E"

def get_ids(ip,ip_class):
    #class A
    if(ip_class=="A"):
        print("Network id : "+ip[0])
        print("host id : ",".".join(ip[1:4]))
    if(ip_class=="B"):
        print("Network id : ",".".join(ip[0:2]))
        print("host id : ",".".join(ip[2:4]))
    if(ip_class=="C"):
        print("Network id : ",".".join(ip[0:3]))
        print("host id : ",str(ip[3]))
    else:
        print("This network ip cannot be divided into Network and host IDs")

#driving code block :
ip = "192.168.0.101"
ip = ip.split(".")      #makes the octets into elements of a tuple
print("ip = ",ip)
ip  = [int(i) for i in ip]  #taking all the values of ip one by one
ip_class = getclass(ip)
print("Given IP belongs to class : ",ip_class)

ip  = [str(i) for i in ip] #printinf the network and host ids
get_ids(ip,ip_class)
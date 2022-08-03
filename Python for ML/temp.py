# python_list
friends = ["soma","bunny","hoods","bunnu"]
print(type(friends))
print(friends[3])
print(friends[-1])
print(friends)
campsite = ["Lake Clears",404,89.3,True]
friends.append("vinayak") #adds only one piece of data
print(friends)

#to add multiple data values , add a list to a list by using .extend method
#or use the insert(index,"item") method
#or use the concatenation way
list1 = ["laptop","desktop","mouse","keyboard"]
list1.extend(["dactyle keyboard","Raspberry Pi4","Lcd 10in","Linux"])
list1 += ["Headset","Microphone","usb"]
list1.insert(-1,"ROG") 
print("List1 = ",list1)

#how to remove things from list
list1.remove("desktop")     #removes one specified object from list
list1.pop(0)        #pop(index)

# *also remember that the pop() method also returns the value the data it popped
print("The removed data was : ",list1.pop(0))
list1.clear()   #it' clear every item from the list
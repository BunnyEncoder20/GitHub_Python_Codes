print("Hello World")
print("I am Iron Man")
print("I am Thor Odinson")

# this is a comment

print("""
This is a 
multi line
print statement !
""")
#this uses 3 double qoutes 

print("Line one "+"Line two "+"Line Three")
print("Line one \n"+"Line two\n"+"Line Three\n")
print("Repeat this line 5 times\n"*5)

#Robo Senpai Barista !
print("Hello, Welcome to Soma Senpai Cafe !\n")
name=input("What is your Name ?\n")
print("Hi, "+name+". What can I get ya today?")
print("""Menu :
1. Coffee
2. Tea
3. Milk
4. Special Senpai Milk""")
item = input()
print("Okay! One "+item+" coming right UP !")

#temp2.py part
# from msilib import type_string


# name = "Bunny"
# age = 21
# print(name)
# print(type(name))
# print(age)
# print(type(age))

# # age='21'
# # print(type(age)) prints the 

# accurate_age = 21.5
# print(accurate_age)
# print(type(accurate_age))

# expo = 5**2 #use double * for rasing 5 to power of 2
# print("Exponents : 5^2 = ",expo)

print("Welcome to Some Senpai cafe !")
name = input("What is your name ?\n")
print("Ok "+name+", What would you like to order ?")
item = input("""~~~Menu~~~ 
1. Coffee   $8
2. Tea        $8
3. Milk       $8
4. Special Milk     $8\n""")
print("Ooo "+item+" Good Choice!")
number=input("How many of those would you like ??\n")
total = 8*int(number) #it is important to convert the number to a int because by default it is stored as  a string
#the error was occuring because the 8 was getting multiplied by the string value of "2" number
print(number," "+item+" will be ready shortly")

print("Your grand total is = "+str(total)) #can also convert the int value to string to print it or just a simple ,
print("Your grand total is = ", 8*int(number))
print("Thank you for coming to Soma's Cafe! Enjoy !")

# temp3.py
name=input("What is your name?\n")
if name == "bunny" or name=="Bunny":
    print("Oh you are not welcome here, get out !")
    exit()  #this terminates the program
else :
    print("Oh, welcome "+name+" make yourself comfy!")

#remember indentation is important in python 

if 4<3:
    print("True!")
else:
    print("False")

#temp5.py
name = input("What is you name ?")
if name=="bunny" or name=="Bunny":
    naughty = input("Are you naughty?")
    if naughty=="Yes" or naughty=="yes":
        print("Then you cannot enter here. Good bye!")
        exit()
    else:
        print("Oh, then there is no problem")

print("Welcome to the Senpai Cafe !")

print("""~~~MENU~~~
1.Coffee        $8
2.Tea             $5
3.Milk            $2
4.Special Milk  $15""")
item=input("What would you like to have?\n")
if item=="coffee":
    price=8;
elif item=="tea":
    price=5;
elif item=="milk":
    price=5;
elif item=="special milk":
    price=15;
else:
    print("Oh, we don't have that here righht now,\nCome back Later!")
    exit()
number=input("Oo "+item+" good choice. How mnay of those would you like?")
print("You grand total = ₹", int(number)*int(price))

#temp6.py
name = input("What is you name ?")
if name=="bunny" or name=="Bunny" :
    naughty = input("Are you naughty?")
    if naughty=="Yes" or naughty=="yes":

        print("Then you cannot enter here. Good bye!")
        exit()
    else:
        print("Oh, then there is no problem")

print("Welcome to the Senpai Cafe !")

print("""~~~MENU~~~
1.Coffee        $8
2.Tea             $5
3.Milk            $2
4.Special Milk  $15""")
item=input("What would you like to have?\n")
if item=="coffee":
    price=8;
elif item=="tea":
    price=5;
elif item=="milk":
    price=5;
elif item=="special milk":
    price=15;
else:
    print("Oh, we don't have that here righht now,\nCome back Later!")
    exit()
number=int(input("Oo "+item+" good choice. How mnay of those would you like?"))
print("You grand total = ₹", number*int(price))
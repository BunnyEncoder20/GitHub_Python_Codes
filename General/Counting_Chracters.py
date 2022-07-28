'''
Q) Given a string S, write a program to count the occurrence of 
Lowercase characters, Uppercase characters, Special characters 
and Numeric values in the string.
Note: There are no white spaces in the string
'''
def char_count(str1):
    special="!@#$%^&*~:;,.<>/?\|-+=`"
    upper,lower,num,specialsym=0,0,0,0
    for i in str1 :
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i.isnumeric():
            num+=1
        elif i in special:
            specialsym+=1
    print("\nUppercase : ",upper,"\nLowercase : ",lower,"\nNumbers : ",num,"\nSpecial Symbols : ",specialsym)

#driver code
str1=input("Enter the string : ")
char_count(str1)

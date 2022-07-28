import os
def goodORbad(ch):
    charset=[False]*126
    checkchar=ch.lower()
    for i in range(0,len(ch)):
        val=ord(checkchar[i])
        if charset[val]:
            return ("Does not contain Unique Characters\n\n")
        else :
            charset[val]=True
    return ("Unique Chracters in this string\n\n")

os.system("cls")
ch=input("Enter the String :\n")
print(goodORbad(ch))
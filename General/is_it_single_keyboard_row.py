'''
Q)  Given an  English word,  write an algorithm and the subsequent Python code 
    to check if the given word can be typed using just a single row of the
    keyboard.(e.g. POTTER, EQUITY). Print 'Yes' if the letters of the word are 
    from a single row and print 'No' otherwise.

Input format:

A word

Output format:

Print ‘Yes’ if all letters of the word are from same row in a keyboard
'''
def KeyboardRowCheck(word):
    text=word.lower()
    row1="qwertyuiop"
    row2="asdfghjkl"
    row3="zxcvbnm"

    f=True
    if text[0] in row1:
        for i in text:
            if i not in row1:
                f=False
    else:
        if text[0] in row2:
            for i in text:
                if i not in row2:
                    f=False
        else :
            if text[0] in row3:
                for i in text:
                    if i not in row3:
                        f=False
    if f==True:
        return("yeah ha Boii")
    else:
        return("Nope")
    
#Driver Code:
import os
os.system("cls")
word=input("Enter the word : ")
print(KeyboardRowCheck(word))

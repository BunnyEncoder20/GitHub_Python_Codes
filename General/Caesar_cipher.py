'''
Q)In Caesar cipher, each letter is replaced by another letter which occurs at 
the  d-th position (when counted from the position of the original letter), in
the  English alphabet. For identifying the position of a letter, we follow the
usual order of the English alphabet, from a to z. Given a word and a positive 
integer d, use Caesar cipher to encrypt it. For example, if the word is 'ball' 
and the value of 'd' is 3 then the new encrypted word is 'edoo'. 'x' will be 
replaced by 'a', 'y' should be replaced by 'b' and 'z' should be replaced by 
'c'. While the code is submitted for Online Judge (SkillRack), use rstrip(), 
to remove carriage return character in the input.

Input Format
Word
A positive integer 'd'
Output format:
Encrypted word
'''
#Code for Ceasar Encryption and Decryption :
def Encryption(word,shift):
    result=""
    for i in range(len(word)):
        char=word[i]
        
        if char.isupper():
            result+=chr((ord(char)+shift-65)%26+65)
        else:
            result+=chr((ord(char)+shift-97)%26+97)
    print(result)

def Decryption(word,shift):
    result=""
    for i in range(len(word)):
        char=word[i]
        
        if char.isupper():
            result+=chr((ord(char)-shift-65)%26+65)
        else:
            result+=chr((ord(char)-shift-97)%26+97)
    print(result)

ch=int(input("Select 1)Encryption or 2)Decryption\n"))
word=input("Enter the word : ")
shift=int(input("Enter the Shift value : "))
if ch==1:
    Encryption(word,shift)
else:
    Decryption(word,shift)

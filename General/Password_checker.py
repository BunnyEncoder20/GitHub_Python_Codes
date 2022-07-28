'''
Q)Given a word, check if it is a valid password or not.  A password is said to 
be valid if it satisfies the following conditions:
i) Should begin with a letter
ii) Should contain atleast one digit and one special character
iii) Length of the password should be atleast 8
Print ‘Valid' if the given word satisfies the above three conditions  and
 print ‘Invalid’ otherwise.

Input format:
A word
Output format:
Print ‘Valid' if the given word satisfies the above three conditions  and 
print ‘Invalid’ otherwise.
'''

def check_password(password):
    if password[0].isalpha():
        if len(password)>=8:
            if any(not i.isalnum() for i in password) and any(i.isnumeric() for i in password):
                return("Valid")
            else:
                return("Invalid : Password must have atleast one number and special character!")
        else:
            return("Invalid : Password should have at least 8 characters!")
    else:
        return("Invalid : Password should begin with a letter!")

#driver code:
password=input("Enter Password : ")
print(check_password(password))

'''
Q)  Write a Python Script to find the multiples of a given number up to a specific 
    range.

Input:
Number
range

Output:
Multiples of a number.
For example, if a Number is 5 and range is '3' , the output is 5 10 15
if a number is 3 and range is '4', the output is 3 6 9 12
'''
def funky(num,limit):
    counter=1
    while counter<=limit:
        x=num*counter
        print(x)
        counter+=1

num=int(input("Enter the number : "))
limit=int(input("Enter the Range : "))
funky(num,limit)


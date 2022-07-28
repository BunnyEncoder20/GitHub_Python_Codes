def rev_tri (rows):
    k = 2 * rows - 2  
 
    for i in range(rows, -1, -1):  
        
        for j in range(k, 0, -1):  
            print(end="#")
            for j in range(0, i + 1):  
                print("*", end=" ")  
            print("")  
            k = k + 1  

        

#Driver code 
pattern_numbers=int(input("Enter the number of rows : "))
r=[]
for i in range(0,pattern_numbers):
    x = int(input())
    r.append(x)
for i in r:
    rev_tri(i)
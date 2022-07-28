n=int(input())
lines=[] ; v_l=[] ; h_l=[]
for i in range(n):
    a=int(input())
    b=int(input())
    lines.append([a,b])


for i in lines:
    for j in lines:
        if i!=j:
            if i[1]==j[1] and i[0]<j[0]:
                
                x=[]
                x.append(i)
                x.append(j)
                v_l.append(x)
                h_l.append(x)
            
            elif i[0]==j[0] and i[1]<j[1]:
                x=[]
                x.append(i)
                x.append(j)
                
                v_l.append(x)

step=[]
len=[]

for i in h_l:
    x=[i]
    for j in l:
        if i!=j:
            if x[-1][1]==j[0]:
                x.append(j)
        if len(x)!=1:
            step.append(x)
            len.append(len(x))
final=[]
m=0
for i in len:
    if i>m:
        m=i
for i in step:
    if len(i)==m:
        if i not in final:
            final.append(i)

for i in final:
    print(i)
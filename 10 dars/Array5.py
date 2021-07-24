l=[0,1]
A1=0
A2=1
n=8
for i in range(n-2):
    A3=A1+A2
    l.append(A3)
    A1=A2
    A2=A3
    
print(l)
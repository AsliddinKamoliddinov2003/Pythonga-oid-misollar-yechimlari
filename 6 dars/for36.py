import math
n=int(input('n = '))
k=int(input('k = '))
s=0
for i in range(1,n+1,1):
    for j in range(n):
        l=math.pow(i,k)
    s+=l        
    print(s)
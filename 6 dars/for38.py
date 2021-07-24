import math
n=int(input('n = '))
s=0
for i in range(1,n+1,1):
    for j in range(n):
        l=math.pow(i,n+1-i)
    s+=l        
    print(s)
import math
n=int(input('n = '))
temp=n
k=0
while not n<=0:
    temp-=3
    if pow(3,k)==n:
        break
    k+=1
   
print(k)
else


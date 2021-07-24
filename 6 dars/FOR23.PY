import math
x=1
k=0
isho=0
n=int(input('n = '))
for i in range(0,n+1,1):
    isho=((-1)**(i+1))
    k+=(math.pow(x,2*i-1)/(math.factorial(2*i-1)))
  
print(k)


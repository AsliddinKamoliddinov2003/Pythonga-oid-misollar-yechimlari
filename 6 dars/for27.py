import math
k=float(0)
x=float(0)
n=float(input('n = '))
for i in range(0,n+1):
    k+=((2*i-1)*(math.pow(x,2*i-1)))/((2*i)*(2*i+1))
  
print(k)


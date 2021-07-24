import math
n=int(input('n = '))
x=float(input('x = '))
sum=0
y=0
for son in range(1,n+1,1):
    isho=(-1)**(son+1)
    i=((math.pow(x,son)/son))
    sum+=i*isho
   
    
print(f'sum = {sum}')
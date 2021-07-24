max=-float('inf')
min=float('inf')
flag=True
t=0
N=5
for i in range(N):
    son=int(input('son = '))
    if son<min or son>max:
        min=son
        max=son
        t+=1

print(t)
        

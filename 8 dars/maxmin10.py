max=-float('inf')
min=float('inf')
t=0
N=5
for i in range(N):
    son=int(input('son = '))
    if son<min and son>max:
        min=son
        max=son
    
print(max or min)
        

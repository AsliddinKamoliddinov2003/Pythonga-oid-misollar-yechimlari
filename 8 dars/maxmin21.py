N=5
max=-float('inf')
min=float('inf')
k=0
t=0
for i in range(N):
    son=int(input('son  = '))
    if max<son:
        max=son
        t+=1
    
    if min>son:
        min=son
        k+=1
    

print(((son-(min*k+max*t))/N-(k+t)))


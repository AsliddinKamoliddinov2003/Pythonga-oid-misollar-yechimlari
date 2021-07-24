N=6

max=-float('inf')
maxx=-float('inf')
min=float('inf')
flag=True
t=0
k=0
for i in range(N):
    son=int(input('son = '))
    if son>max and flag:
        max=son
        if i!=0:
            t+=1
            flag=False
    if maxx<son:
        maxx=son
        k+=1
    if maxx=max:
        print('0')
    
print(N-(k+t))

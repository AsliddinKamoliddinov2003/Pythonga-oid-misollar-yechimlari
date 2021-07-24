N=10
max=7
min=float('inf')
t=0
for i in range(N):
    son=int(input('son = '))
    if max<son:
        son=max
        if min<max:
            min=son
            t+=1
            print(t)
else:
    print('0 0') 

    

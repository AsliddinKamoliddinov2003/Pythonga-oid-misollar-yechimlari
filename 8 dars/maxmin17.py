N=5
max=-float('inf')
t=0
for i in range(N):
    son=int(input('son = '))
    if max<son:
        max=son
        t+=1
print(N-t)
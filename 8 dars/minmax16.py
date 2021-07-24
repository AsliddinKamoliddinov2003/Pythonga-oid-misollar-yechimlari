N=5
min=float('inf')
t=0
for i in range(N):
    son=int(input('son = '))
    if min>son:
        min=son
        t+=1
print(t-1)
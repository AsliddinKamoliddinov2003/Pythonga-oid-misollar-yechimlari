N=3
max=-float('inf')
min=float('inf')
flag=True

for i in range(N):
    son=int(input('son = '))
    if son>max and flag:
        max=son
        if i!=0:
            flag=False
    if min>son:
        min=son

print(min,max)
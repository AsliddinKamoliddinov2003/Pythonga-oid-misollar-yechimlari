N=3
max=-float('inf')
min=float('inf')
flag=True

for i in range(N):
    son=int(input('son = '))
    if son<min and flag:
        min=son
        if i!=0:
            flag=False
    if max<son:
        max=son

print(min,max)
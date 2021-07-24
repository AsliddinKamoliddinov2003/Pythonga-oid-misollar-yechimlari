N=3
max=-float('inf')
flag=True

for i in range(N):
    son=int(input('son = '))
    if son>max and flag and son%2==1:
        max=son
        if i!=0:
            flag=False
print(max)
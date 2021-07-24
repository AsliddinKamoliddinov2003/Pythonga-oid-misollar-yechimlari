N=5
min=float('inf')

for i in range(N):
    son=int(input('son = '))
    if min>son and son>0:
        min=son
print(min)
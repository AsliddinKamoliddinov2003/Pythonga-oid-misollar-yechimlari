N=5
max=-float('inf')
min=float('inf')
for i in range(N):
    number=int(input('Son = '))
    if max<number:
        max=number
    if min>number:
        min=number

print(f'max = {max}')   
print(f'min = {min}')
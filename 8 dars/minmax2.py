N=5
min=float('inf')
for i in range(N):
    a=int(input('a = '))
    b=int(input('b = '))
    number=(a*b)
    if min>number:
        min=number

 
print(f'min = {min}')
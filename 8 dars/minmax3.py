N=5
max=-float('inf')
for i in range(N):
    a=int(input('a = '))
    b=int(input('b = '))
    number=((a+b)*2)
    if max<number:
        max=number

 
print(f'max = {max}')
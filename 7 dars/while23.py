a=int(input('a = '))
b=int(input('b = '))

while a!=b:
    if a>b:
        a-=b
    elif b>a:
        b-=a

print(a)
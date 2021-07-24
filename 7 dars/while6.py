n=int(input('n = '))
s=1
while n>0:
    if n%2==0:
        s*=n
        n-=2
        print(s)
    else:
        s*=n
        n-=2
        print(s)
        
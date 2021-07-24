n=int(input('n = '))
oxirgi_raqam=0
f1=0
f2=1
f3=1
while n>0:
    oxirgi_raqam=n%10
    f3=f1+f2
    f1=f2
    f2=f3
    if oxirgi_raqam==f3:
        print(f'bor')
        break
    n//=10


else:
        print(f'yoq')
        
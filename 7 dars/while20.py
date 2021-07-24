n=int(input('n = '))
oxirgi_raqam=0
while n>0:
    oxirgi_raqam=n%10
    print(oxirgi_raqam, end=" ")
    if oxirgi_raqam==2:
        print(' ')
        print(f'2 raqami bor')
        break
    n//=10


else:
        print(f'yoq')

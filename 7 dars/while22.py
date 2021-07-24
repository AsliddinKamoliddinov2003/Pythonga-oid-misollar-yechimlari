n=int(input('n = '))
oxirgi_raqam=0
while n>0:
    oxirgi_raqam=n%10
    print(oxirgi_raqam, end=" ")
    if not oxirgi_raqam/1==oxirgi_raqam and oxirgi_raqam/oxirgi_raqam==1:
        print(' ')
        print(f'toq son bor')
        break
    n//=10


else:
        print(f'yoq')

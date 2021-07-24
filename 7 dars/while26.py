n=13
f1=0
f2=1
f3=1
t=0
while not n<0:
    f3=f2+f1
    f1=f2
    f2=f3

    if f3==n:
        tem=f3
        print(f'{tem+f1} _____ {f3-f2+f1}')

        
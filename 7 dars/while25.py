n=3
f1=0
f2=1
f3=1
while not n<0:
    f3=f2+f1
    f1=f2
    f2=f3

    if f3>n:
        print(f'{f3}')
        break

        
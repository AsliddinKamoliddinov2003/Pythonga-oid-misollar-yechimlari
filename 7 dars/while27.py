n=34
f1=0
f2=1
f3=1
t=0
while f3<n:
    f3=f2+f1
    f1=f2
    f2=f3
    t+=1
    if n==f3:
        print(t+2)

        
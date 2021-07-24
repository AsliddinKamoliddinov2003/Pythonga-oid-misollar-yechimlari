a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
if (a!=b!=c) and (a<b<c):
    print(a,c)
if (a!=b!=c) and (a>b>c):
    print(c,a)
if (a!=b!=c) and ((a>b<c) and (a>c)):
    print(a,c)
if (a!=b!=c) and ((a>b<c) and (a<c)):
    print(c,a)


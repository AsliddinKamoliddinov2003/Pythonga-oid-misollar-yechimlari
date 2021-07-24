a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
d=int(input("d = "))
if a==b and b==c:
    print(d)
if a==c and c==d:
    print(b)
if a==b and b==d:
    print(c)
if c==d and d==b:
    print(a)
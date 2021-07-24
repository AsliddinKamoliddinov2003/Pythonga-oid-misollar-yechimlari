a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
if a<b and a<c:
    print(f"b + c = {b+c}")
if a>b and b<c:
    print(f"a + c = {a+c}")
if c<b and a>c:
    print(f"b + a = {b+a}")
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
if a<b and b<c:
    print(f"a = {2*a}, b = {2*b}, c = {2*c}")
if a>b and b>c:
    print(f"a = {2*a}, b = {2*b}, c = {2*c}")
else:
    print(f"a = {-a}, b = {-b}, c = {-c}")
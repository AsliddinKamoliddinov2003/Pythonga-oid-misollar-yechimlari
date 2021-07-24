x=int(input("sonni kiriting 3 xonali bo'lsin = "))
y=x%10
z=x//10
b=z%10
h=x//100
print(f"birlar xonasidagi son = {y}")
print(f"o'nlar xonasidagi son = {b}")
print(f"yuzlar xonasidagi son = {h}")
print(f"raqamlar yig'indisi = {y+b+h}")
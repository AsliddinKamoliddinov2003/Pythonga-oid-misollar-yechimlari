x=int(input("x = "))

a=x%10
b=(x//10)%10
c=x//100

print((a!=b and b!=c and c!=a))
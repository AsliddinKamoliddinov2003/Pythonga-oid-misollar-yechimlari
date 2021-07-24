x=int(input("x = "))
c=x//100
b=(x//10)%10
a=x%10


print((c<b and b<a )or (c>b and b > a))
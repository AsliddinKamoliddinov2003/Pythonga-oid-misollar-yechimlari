a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
print(((a*a+b*b)**(1/2))==c or ((a*a+c*c)**(1/2))==b or ((b*b+c*c)**(1/2))==a)
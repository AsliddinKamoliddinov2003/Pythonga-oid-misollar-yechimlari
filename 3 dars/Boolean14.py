
A=int(input("A = "))
B=int(input("B = "))
C=int(input("C = "))
x=((A>0 or B<0 or C<0) and (A<0 or B>0 or C<0) and (A<0 or B<0 or C>0)) 
print(x)
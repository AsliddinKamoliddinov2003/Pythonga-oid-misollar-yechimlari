A=int(input('A = '))
B=int(input('B = '))
C=int(input('C = '))
t=1
s=1
while A>C:
    A=A//C
    t+=1    
while B>C:
    B=B//C
    s+=1    
print(t*s)
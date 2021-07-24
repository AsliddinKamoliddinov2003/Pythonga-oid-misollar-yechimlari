A=int(input("A = "))
B=int(input("B = "))
l=abs(A-B)
s=0
for i in range(A,B+1,1):
    s+=1
    for son in range(s):
        print(i)
    
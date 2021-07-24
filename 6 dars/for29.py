A=float(input("A = "))
B=float(input("B = "))
n=int(input("n = "))
l=abs(A-B)
t=l/n
k=0
for i in range(n):
    k+=t
    print(k)
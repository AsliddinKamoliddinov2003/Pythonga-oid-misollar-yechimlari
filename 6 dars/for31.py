n=int(input("n = "))
k=0
A0=2
for i in range(n):
    A=2+1/A0
    A0=A
    k+=1
    print(f'A{k}={A}')
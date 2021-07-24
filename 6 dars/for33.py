n=int(input("n = "))
k=0
A1=1
A2=1
for i in range(n):
    
    A3=A2+A1
    A1=A2
    A2=A3
    
    k+=1
    
    print(f' A{k}={A3}')
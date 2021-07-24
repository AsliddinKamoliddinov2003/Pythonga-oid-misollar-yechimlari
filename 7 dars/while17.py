n=int(input("n = "))
m=int(input("m = "))
butun=0
while not n<=m:
    n=n-m
    butun+=1
    
print(f"butun qismi =  {butun} n={n}")
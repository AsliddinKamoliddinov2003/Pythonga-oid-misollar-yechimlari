A=input("A = ")
B=input("B = ")
C=input("C = ")
A=int(A)
B=int(B)
C=int(C)
D=B*B-4*A*C
if D>0:
    print(f"2 ta yechimga ega")
elif D==0:
    print(f"1 ta yechimga ega")
else:
        print(f"yechimga ega emas!")
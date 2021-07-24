a=int(input("a = "))
b=int(input("b = "))
yigindi=0
S=0
for son in range(a,b+1,1):
    yigindi=yigindi+a
    S+=1/yigindi
else:
    print(S)
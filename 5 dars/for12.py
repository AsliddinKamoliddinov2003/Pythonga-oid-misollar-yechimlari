n=int(input("n = "))
yigindi=0
vvv=1
for son in range(1,n+1,1):
    yigindi=(son/10+1)
    vvv*=yigindi
else:
    print(vvv)
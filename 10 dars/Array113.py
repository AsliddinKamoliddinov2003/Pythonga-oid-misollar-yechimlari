n=[-5,-1,4,3,2,8]

for f in range(0,len(n)):
   print(n[f])
vaqtincha=int

for i in range(0,len(n)):
    for j in range(0,i):
        if n[i]>n[j]:
            vaqtincha=n[i]
            n[i]=n[j]
            n[j]=vaqtincha
for i in range(len(n)-1,-1,-1):
    print(n[i])
           
            

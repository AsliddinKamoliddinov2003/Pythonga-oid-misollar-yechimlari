n=[5,4,3,2,0,1,6,9,8]

vaqtincha=int

for i in range(0,len(n)):
    for j in range(0,i):
        if n[i]>n[j]:
            vaqtincha=n[i]
            n[i]=n[j]
            n[j]=vaqtincha
for i in range(len(n)-1,-1,-1):
    print(n[i])
           
            

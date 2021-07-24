n=[1,3,-6,9,-5,3,-7,6]

for i in range(0,len(n)-1):
    if (n[i]*(n[i]+1))<0:
        
        print(0)
        break
else:
    print(n[i])
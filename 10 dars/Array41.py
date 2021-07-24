n=[1,2,0,7,9,3,2,1,4,6]
l=[]
yigindi=0
for i in range(0,len(n)-1):
    yigindi=(n[i]+n[i+1])
    l.append(yigindi)  
        
print(max(l),n[i],n[i+1])


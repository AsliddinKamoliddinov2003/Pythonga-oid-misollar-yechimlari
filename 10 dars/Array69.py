n=[1,2,3,4,5,6,7,8]
b=[]
for i in range(1,len(n)-1,2):
        
    n[i],n[i+1]=n[i+1],n[i]
    print(n)
    


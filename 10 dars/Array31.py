n=[1,2,1,9,5,5,4]
b=[]

for i in range(0,len(n)):
    if n[i-1]<n[i]:
        print(n.index(i))
       



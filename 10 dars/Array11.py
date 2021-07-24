n=[1,2,3,4,5,6,7,8,9,10]
l=[]
k=3
for i in range(0,len(n)+1,1):
    if i%3==0 and i!=0:
        l.append(i)
    
print(l)
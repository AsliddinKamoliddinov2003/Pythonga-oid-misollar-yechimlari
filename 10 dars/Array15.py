n=[1,2,3,4,5,6,7,8,9,10]
l=[]
k=3
for i in range(0,len(n)+1,1):
    if i%2==1:
        l.append(i)
    

for j in range(len(n),-1,-2):
    if i%2==0:
        l.append(j)
print(l)
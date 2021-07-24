n=[1,2,3,4,5,6,7,8,9,-2]

sanoq=0
for i in range(0,len(n)+1):
    if n[i]!=n[i+1]:
        sanoq+=1
    
print(sanoq)
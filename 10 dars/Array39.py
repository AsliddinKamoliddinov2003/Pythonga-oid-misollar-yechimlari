n=[1,2,0,7,9,3,2,1,4,6,5]

sanoq=0
for i in range(len(n)-1):
    if not n[i]<n[i+1] or n[-1]<n[-2]:
        sanoq+=1
if n[-1]>n[-2] or n[-1]<n[-2]:
    sanoq+=1

print(sanoq)
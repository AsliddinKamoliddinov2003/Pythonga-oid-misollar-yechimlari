n=[1,2,4,6,1,7,2,6,9,4,2,8,6,3]

_min=float('inf')
for i in range(0,len(n)+1):
    while n[i-1]<n[i]>n[i+1]:
        if _min>n[i]:
           _min=n[i]
           break
        
    print(_min)
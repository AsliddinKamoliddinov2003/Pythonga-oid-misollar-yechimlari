n=[8,6,9,4,2,3,7,5,1,8,6,4,2,3]

for i in range(0,len(n)):
    if n[i-1]>n[i]<n[i+1]:
        print(n[i]**2)
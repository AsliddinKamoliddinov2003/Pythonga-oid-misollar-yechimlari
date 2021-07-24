n=[1,2,4,5,1,7,2,6,9,4,2,8,6,3]


for i in range(0,len(n)):
    if n[i-1]<n[i]>n[i+1]:
        print(i)
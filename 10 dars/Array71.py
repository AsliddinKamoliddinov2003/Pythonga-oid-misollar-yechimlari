a=[1,2,3,4,5,6,7,8,9,12,13]
for i in range(1,len(a)):
    a[i-len(a)],a[i]=a[i],a[i-len(a)]
    print(a[len(a)-i])
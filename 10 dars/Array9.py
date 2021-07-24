l=[4,5,7,8,6,9]
sanoq=0
for i in range(len(l)-1,-1,-1):
    if l[i]%2==0:
        print(l[i])
        sanoq+=1

print('juft sonlat = ',sanoq)
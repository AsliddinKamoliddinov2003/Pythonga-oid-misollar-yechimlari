a=[1,2,3,4,5,6,7,8,9,10]
b=[]
sanoq=0
for i in range(1,len(a)+1,2):
    sanoq+=1
    b.append(a[i])
    print(i)
    
print('____________________________________________________________')
    
print(f'soni = {sanoq}')

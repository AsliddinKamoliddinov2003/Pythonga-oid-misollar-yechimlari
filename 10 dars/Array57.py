a=[1,2,3,4,5,6,7,8,9,10]
b=[]

for i in range(0,len(a),2):
    b.append(a[i])
for j in range(1,len(a)+1,2):
    b.append(a[j])

print(b)
    
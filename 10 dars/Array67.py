n=[5,6,8,7,2,9,12,13,17,15]
b=[]
c=[]

for i in range(0,len(n)):
    if n[i]%2==1:
        b.append(n[i])
print(b)

for j in range(0,len(b)):
    c.append(b[j]+b[-1])

print(c)

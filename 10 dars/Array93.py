n=[1,2,7,4,1,9]
c=[]

for i in range(1,len(n)+1,2):
    n.pop(i)
    c.append(n[i])
print(n)
print(len(c))
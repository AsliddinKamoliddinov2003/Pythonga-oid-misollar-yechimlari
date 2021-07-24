n=[1,2,3,4,5,6]
c=[]

for i in range(0,len(n)):
    if n[i]%2==1:
        n.remove(i)
        c.append(n)

print(n)
print(len(c))
    
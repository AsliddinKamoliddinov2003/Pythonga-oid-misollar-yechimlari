n=[1,2,3,4,5,6,7]

for i in range(0,len(n)):
    k=min(n)
    m=max(n)
    l=n.index(k)
    v=n.index(m)
n.insert(l+1,0)
n.insert(v+1,0)

print(n)
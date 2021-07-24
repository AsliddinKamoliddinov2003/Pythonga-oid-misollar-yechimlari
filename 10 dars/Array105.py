n=[1,-2,3,4,5,6]
k=4
m=3
for i in range(0,len(n)):
    if k==i:
        n.insert(k+1,0)

print(n)

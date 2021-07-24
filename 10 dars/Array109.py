n=[1,-2,3,4,5,6,7,8,9]

for i in range(0,len(n)):
    if n[i]<0:
        n.insert(i+1,0)

print(n)
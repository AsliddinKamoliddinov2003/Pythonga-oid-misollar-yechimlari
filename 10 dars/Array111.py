n=[1,2,2,4,1,9]

for i in range(0,len(n)):
    if n[i]%2==1:
        n.append(n[i])
        n.append(n[i])

print(n)
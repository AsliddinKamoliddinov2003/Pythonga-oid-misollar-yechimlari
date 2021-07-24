n=[1,-2,3,4,5,6]

for i in range(1,len(n)+1,2):
    n.append(n[i])
    n.append(n[i])

print(n)
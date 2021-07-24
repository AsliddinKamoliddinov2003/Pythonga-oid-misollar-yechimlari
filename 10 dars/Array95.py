n=[1,2,2,4,1,9]

for i in range(1,len(n)+1,1):
    if n[i]==n[i+1] in n:
        n.remove(n[i])

print(n)
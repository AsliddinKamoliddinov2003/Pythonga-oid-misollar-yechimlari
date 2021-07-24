n=[1,2,3,4,5,6,7,8,9]

for i in range(1,len(n)+1):
    if 0<i<5:
        n.pop(n[i])

print(n)
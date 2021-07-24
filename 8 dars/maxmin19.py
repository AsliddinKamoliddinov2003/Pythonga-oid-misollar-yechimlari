N=5
t=0
min=float('inf')

for i in range(N):
    son=int(input('son = '))
    if min>son:
        min=son
    

k=min
for j in range(son):
    if k==son:
        t+=1

print(t)


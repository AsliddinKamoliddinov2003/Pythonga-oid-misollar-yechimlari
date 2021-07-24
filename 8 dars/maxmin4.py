N=5
_min=float('inf')
_min_indeks=0
for i in range(N):
    son=int(input('son = '))
    if _min>son:
        _min=son
        _min_indeks=i

print(_min_indeks)
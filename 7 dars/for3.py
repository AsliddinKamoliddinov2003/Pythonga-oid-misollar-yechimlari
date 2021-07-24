N=int(input('N = '))
K=int(input('K = '))
sanoq=0
while N>K:
    N=N-K
    sanoq+=1
print(f'qoldiq = {N}')
print(f'Butun = {sanoq*K}')
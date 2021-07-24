N=5
max=-float('inf')
for i in range(N):
    m=int(input('m = '))
    v=int(input('v = '))
    zichlik=(m/v)
    if max>zichlik:
        max=zichlik

 
print(f'max = {zichlik}')
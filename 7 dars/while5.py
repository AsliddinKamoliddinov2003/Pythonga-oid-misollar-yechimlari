n=int(input('n = '))

sanoq=0
son=2
daraja=1
while daraja<=n:
    daraja*=son
    sanoq+=1
print(sanoq-1)
n=[5,1,2,3,8,5,2,7,8,9,10]


K=3
L=6
yig=0
sanoq=0
for i in range(K+1,L):
    yig+=n[i]
    sanoq+=1
    arf=yig/sanoq
    
print(arf)

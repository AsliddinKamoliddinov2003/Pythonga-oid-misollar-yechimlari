pul1=int(input('pul1 = '))
p=int(input('foiz = '))
hozirgi_pul=pul1
oy=0
while hozirgi_pul<pul1*2:
    hozirgi_pul*=(1+(p/100))
    oy+=1
    
print(oy) 
    
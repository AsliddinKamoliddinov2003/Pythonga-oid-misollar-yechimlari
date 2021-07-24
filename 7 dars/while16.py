ku1=10
p=int(input('foiz = '))
hozirgi_yol=ku1
kun=0
S=0
while hozirgi_yol<=200:
    hozirgi_yol*=(1+(p/100))
    kun+=1
    s=ku1+hozirgi_yol
print(kun) 
print(s)
    
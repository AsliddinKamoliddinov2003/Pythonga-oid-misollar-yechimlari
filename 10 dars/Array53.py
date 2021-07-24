a=[1,2,3]
b=[4,5,6]
l=[]
for i in range(len(a)):
    m=max(a)
    print(m)
    l.append(m)
    break

   
for i in range(len(b)):
    n=max(b)
    print(n)
    l.append(n)
    break
 
 
print(l)
    

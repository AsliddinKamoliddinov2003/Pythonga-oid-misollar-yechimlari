n=[1,2,3,5,4,8,7,69,7,6]
l=[]
for i in range(1,len(n)+1,2):
    l.append(n[i])


print(max(l))
n=[5,1,2,3,8,5,2,7,8,9,10]

for son in n:
    if son < n[-1] and son > n[0]:
        print(n.index(son))
        break
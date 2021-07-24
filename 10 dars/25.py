n=[2,9,2,4,8,16,32,64,129]

for son in range(0,len(n)+1):
    while n[son+1]%n[son]==0:
        print(n[son+1]/n[son])
        break
    else:
        print(0)
        break
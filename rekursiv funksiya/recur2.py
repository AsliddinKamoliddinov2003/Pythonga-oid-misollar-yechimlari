def fak(n):
    if n%2==0:
        if n==2:
            return 2
        return n*fak(n-2)
    if n%2==1:
        if n==1:
            return 1
        return n*fak(n-2)

print(fak(5))

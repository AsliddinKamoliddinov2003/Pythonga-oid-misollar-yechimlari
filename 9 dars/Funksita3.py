def calculyator(a,b,sign=1):
    if sign==1 or sign=='+':
        return a+b
    if sign==2 or sign=='-':
        return a-b
    if sign==3 or sign=='*':
        return a*b
    if sign==4 or sign=='/':
        return a/b
    print(calculyator(28,4,'/'))
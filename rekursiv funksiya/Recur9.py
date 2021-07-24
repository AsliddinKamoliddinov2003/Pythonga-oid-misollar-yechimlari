def ekub(a,b):
    if a==b:
        print(a)
        return 
    elif a>b:
        a=a-b
    elif b>a:
        b=b-a
    return ekub(a,b)

print(ekub(36,30))
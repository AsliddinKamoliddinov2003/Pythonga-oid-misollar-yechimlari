
def yig(n):
    y=0
    while n>0:
        k=n%10
        y+=k
        p=n//10
        n=p
    return y
   
print(yig(123456))

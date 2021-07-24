
def fib(n,f1=1,f2=1):
    if n!=1:
        print(f1+f2)
        return fib(n-1,f1=f2,f2=f1+f2) 
print(fib(8))
    
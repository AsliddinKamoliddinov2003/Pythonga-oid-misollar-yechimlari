class fac:
    def __init__(self,n):
        self.n=n
        self.i=1  


    def __iter__(self):
        return self
    k=1
    def __next__(self):
        if self.i<=self.n:
            self.k*=self.i
            self.i+=1
            return self.k
        raise StopIteration


for son in fac(10):
    print(son)
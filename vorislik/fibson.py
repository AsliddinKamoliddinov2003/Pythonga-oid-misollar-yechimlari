class fibson:
    def __init__(self,n):
        self.n=n
        self.f1=0
        self.f2=1
        self.i=1  


    def __iter__(self):
        return self

    def __next__(self):
        if self.i<=self.n:
            self.f1,self.f2=self.f2,self.f1+self.f2
            self.i+=1
            return self.f1
        raise StopIteration


for son in fibson(50):
    print(son)
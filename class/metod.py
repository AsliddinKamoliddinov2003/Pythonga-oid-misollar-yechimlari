class person:
    def __init__(self, ism, yosh=0):
        self.name=ism
        self.age=yosh

    def __gt__(self,other):
        return len(self.name) < len(other.name)
    def __eq__(self,other):
        return self.name==other.name
    def __abs__(self):
        if self.age<0:
            self.age*=(-1)
    def __add__(self,other):
        return self.age + other.age
    def __floordiv__(self,other):
        return self.age//other.age
    def __div__(self,other):
        return self.age/other.age
    def __mod__(self,other):
        return self.age%other.age
    def __pow__(self,other):
        return (self.age)**other





odam1=person('Asliddim', 14)
odam2=person('Dildora',44)

print(odam1.age**2)
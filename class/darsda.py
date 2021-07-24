class person:
    def __init__(self,ism,yosh=0):
        self.name=ism
        self.age=yosh

    def __gt__(self,other):
        if len(self.name)>len(self.name):
            return True
        else:
            return False


odam1=person('Komil',21)
odam2=person('Asliddin',18)


print(odam1<odam2)
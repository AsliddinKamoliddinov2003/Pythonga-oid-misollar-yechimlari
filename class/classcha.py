class person:
    _id=1
    name='Asliddin'
    car='spark'
    def __init__(self,_id,name):
        self._id=_id
        self.name=name
tanla=person(2003,'Asliddin')

print(tanla.name)
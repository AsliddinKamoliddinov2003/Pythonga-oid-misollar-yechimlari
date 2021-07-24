class maxsulot:
    def __init__(self,narx):
        self.__narx=narx
    @property
    def price(self):
        return self.__narx
    @price.setter
    def price(self,narx):
        self.__narx=narx
    #price=property(get_narx,set_narx)


banan=maxsulot(5000)
print(banan.price)
banan.price=15000
print(banan.price)
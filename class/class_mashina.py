from random import randint


class mashina:
    def __init__(self,name,volume,benzin,tezlik):
        self.name=name
        self.volume=volume
        self.benzin=benzin
        self.tezlik=tezlik
        self.balon=[10,10,10,10]
    def run(self,km):
        print(f'{(self.name)} {km} km  yol yurdi')
        self.volume=self.volume-km*self.benzin
        print(f'benzin bakida {self.volume}benzin qoldi')
        self.balon[randint(0,3)]  -= 0.5
        print(self.balon)
        if self.volume < 25:
            self.volume+=40
            print(f'mashina {40} litr benzin {self.volume} quydi')
        if self.tezlik>100:
            print(f'radarga tushdingiz 667 ming jarima!!!!!!')
        else:
            print(f'siz namunali haydovchisiz!!!!!!!!!')
        
    def __gt__(self,other):
        return self.volume > other.volume
        


spark=mashina('Spark',28,0.2,120)
captiva=mashina('captiva',40,0.4,60)
spark.run(20)
captiva.run(20)

print(spark.volume)
print(captiva.volume)
print(spark>captiva)
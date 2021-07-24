class moodle:
    def __init__(self,IP,login):
        self.IP=IP
        self.login=login
        print('ochildi')
    def __enter__(self):
        print('qidirilmoqda',self.IP,self.login)
    def __exit__(self,a,b,c):
        print('yuklandi')


with moodle('2003.01.30',7777) as m:
    print('yuklanmoqda')

print('tugatildi')
    
    

class faylni_ochish:
    def __init__(self,filname,mode):
        self.file=open(filname,mode)
    
    def __enter__(self):
        print('kitob ochildi')
        return self.file

    def __exit__(self,a,b,c):
        print('kitob tugadi')
        self.file.close()


with faylni_ochish("kitoblar.txt",'w') as file:
    file.write('ijsvcnidjnv')
print('dastur tugadi')

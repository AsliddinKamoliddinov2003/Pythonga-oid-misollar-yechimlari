file=open('a.txt','r')

while True:
    soz = input('soz :')
    for line in file.readlines():
        
        eng_uzb=line.strip().split(':')
        if soz == eng_uzb[0]:
            print(eng_uzb[1].strip())
file.close()
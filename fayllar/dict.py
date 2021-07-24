soz=input('soz:')

file=open('dictionary.txt','r')
for line in file.readlines():
    uzb_eng=line.strip().split(':')

    if soz==uzb_eng[0].strip():
        print(uzb_eng[1].strip())
    if soz==uzb_eng[1].strip():
        print(uzb_eng[0].strip())


file.close()
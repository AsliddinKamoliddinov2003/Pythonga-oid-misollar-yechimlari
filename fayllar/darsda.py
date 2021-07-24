fayl=open('darsda.txt','r')
for line in fayl.readlines():
    print(line.strip())
fayl.close()
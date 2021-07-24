_id ='20000000'

with open('admins.txt',mode='r') as file:
    qator = file.readline()
    admins=qator.split(';')
    if _id in admins:
        print('siz adminsiz')
        raqam=input('2-ochirish = ')
        if raqam=='2':
            admins.remove(_id)
            
    else:
        print('siz admin emassiz')
        raqam=input('1-qoshish = ')
        if raqam=='1':
            admins.append(_id+';')
content=';'.join(admins)
           
       
with open('admins.txt',mode='w') as file:
    file.write(content)
      


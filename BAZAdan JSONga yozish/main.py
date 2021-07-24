from pathlib import Path
import json
from db_funk import *
from json_funk import create_json_file,add_to_json
from config import JSON_FILE_NAME


main_menu="""
1.DBdan JSONga yozish
2.JSONdan DBga yozish
3.DBdan o'chirish
4. JSONdan o'chirish
#.chiqish"""
first_menu=["Qaysi IDdagi malumotni jsonga yozmoqchisiz : "]

leng_uz={
    "main_menu": main_menu,
    "first_menu": first_menu,
    "ask_user":"Menyudan tanlang: "
    }
while True:
    print(leng_uz["main_menu"])
    key=input(leng_uz["ask_user"])

if key=="1":
    def create_file(filename,data):
        if not Path(filename).exists():
            file=open(filename,"w")
            file.write(data)
            file.close()
    def create_json_file(filename):
        data={
                "all":[]
            }
        create_file(filename,json.dumps(data))
        
    def add_to_json(filename,json_data):
        with open(filename,"r") as  file:
            qator=file.readline()
            full_dict=json.loads(qator)
        full_dict["all"].append(json_data)

        with open(filename,"w") as  file:
            file.write(json.dumps(full_dict))
elif key=="2":
    
   



#create_json_file(JSON_FILE_NAME)


#add_to_json(JSON_FILE_NAME,{"id":9,"name":"Olimjon","age":12,"info":"Til"})
#print(result = read_all())

students=read_all()
for student in students:
    data={
        "id":student[0],
        "name":student[1],
        "age":student[2],
        "info":student[3],
    }

    add_to_json(JSON_FILE_NAME,data)
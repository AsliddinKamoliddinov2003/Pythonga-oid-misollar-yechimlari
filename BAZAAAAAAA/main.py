from db_funk import *
from json_funk import create_json_file,add_to_json
from config import JSON_FILE_NAME

create_json_file(JSON_FILE_NAME)


#add_to_json(JSON_FILE_NAME,{"id":9,"name":"Olimjon","age":12,"info":"Til"})



# result = read_all()

# for row in result:

#     student={
#         "id":row[0],
#         "name":row[1],
#         "age":row[2],
#         "info":row[3]
#     }
    
students=read_all()
for student in students:
    data={
        "id":student[0],
        "name":student[1],
        "age":student[2],
        "info":student[3],
    }

    add_to_json(JSON_FILE_NAME,data)
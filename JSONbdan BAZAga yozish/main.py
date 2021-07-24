import sqlite3
with open("data.json","r") as file:
    tut=file.loads(readlines())
    print(tut)


conn=sqlite3.connect("db.sqlite")
cr=conn.cursor()
sql="""
INSERT INTO users (name,age,info) VALUES (?,?,?);

"""
cr.execute(sql,("Asliddin",18,"Aniq"))
conn.commit()


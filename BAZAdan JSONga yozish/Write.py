import sqlite3

conn=sqlite3.connect("db.sqlite")
cr=conn.cursor()
sql="""
INSERT INTO users (name,age,info) VALUES (?,?,?);

"""
cr.execute(sql,("Asliddin",18,"Aniq"))
conn.commit()

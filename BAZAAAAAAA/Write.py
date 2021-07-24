import sqlite3
from config import DB_NAME

conn=sqlite3.connect(DB_NAME)
cr=conn.cursor()
sql="""
INSERT INTO users (name,age,info) VALUES (?,?,?);

"""
cr.execute(sql,("Asliddin",18,"Aniq"))
conn.commit()

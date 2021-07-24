import sqlite3

conn=sqlite3.connect("db.sqlite")
cr=conn.cursor()
sql="""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    age INTEGER,
    info TEXT
);

"""
cr.execute(sql)
import sqlite3
from config import DB_NAME

conn=sqlite3.connect(DB_NAME)
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
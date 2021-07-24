import sqlite3
from sqlite3 import connect
from config import DB_NAME

conn=sqlite3.connect(DB_NAME)
cr=conn.cursor()


sql="""
CREATe TABLE users(
    year INTEGER,
    month INTEGER,
    day INTEGER
);"""
cr.execute(sql)
conn.commit()
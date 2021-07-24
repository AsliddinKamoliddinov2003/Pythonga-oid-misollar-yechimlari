import sqlite3
from config import DE_NAME

conn=sqlite3.connect(DE_NAME)
cr=conn.cursor() 

sql = """ 
CREATE TABLE users(
    id INTEGER PRIMARY KEY UNIQUE,
    name VARCHAR(255) NOT NULL,
    familya VARCHAR(255),
    age INEGER
    
    
"""

cr.execute(sql)
conn.commit()

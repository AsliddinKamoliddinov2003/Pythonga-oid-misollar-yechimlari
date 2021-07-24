import sqlite3
from config import DE_NAME

conn=sqlite3.connect(DE_NAME)
cr=conn.cursor()

def write(name,otaismi,familya,telraqam,yonalish):
    sql="""
    INSERT INTO users (name,otaismi,familya,telraqam,yonalish) VALUES (?,?,?,?,?);
    """
    cr.execute(sql,(name,otaismi,familya,telraqam,yonalish))
    conn.commit()

def ochir(ID):
    sql="""
    DELETE FROM users WHERE id=?;
    """
    cr.execute(sql, (ID,))
    conn.commit()
    
def oqish():
    sql="""
    SELECT * FROM users;
    """
    result = cr.execute(sql)
    conn.commit()
    return list(result)

def ozgartirish(id,ism,info):
    sql="""
    UPDATE users SET    name = "Messi" WHERE id=4
    """
    cr.execute(sql,(id,ism,info))
    conn.commit()
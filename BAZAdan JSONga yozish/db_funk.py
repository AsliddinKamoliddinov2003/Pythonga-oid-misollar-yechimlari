import sqlite3
from config import DB_NAME

def read_all():
    conn=sqlite3.connect(DB_NAME)
    cr=conn.cursor()
    sql="""
    SELECT * FROM users;
    """
    result=cr.execute(sql).fetchall()
    conn.commit()
    return result

from flask import Flask
import sqlite3
from config import DB_NAME

app = Flask(__name__)

@app.route("/<year>/<month>/<day>/")
def kun(year,month,day):
        
    conn=sqlite3.connect(DB_NAME)
    cr=conn.cursor()
    
    sql="""
    INSERT INTO users   (year,month,day) VALUES(?,?,?);
    """
    result=cr.execute(sql,(year,month,day))
    conn.commit()

    return f"{year}:{month}:{day}"

app.run(debug=True)










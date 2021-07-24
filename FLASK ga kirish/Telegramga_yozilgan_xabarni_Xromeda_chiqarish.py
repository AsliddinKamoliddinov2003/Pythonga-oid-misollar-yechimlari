from flask import Flask
import sqlite3
from config import DB_NAME

app = Flask(__name__)

@app.route("/telegram.org/")
def kun():

    return f"{year}:{month}:{day}"

app.run(debug=True)


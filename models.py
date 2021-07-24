from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import app

db = SQLAlchemy(app)

class News(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('Sarlavha', db.String(255))
    content = db.Column('Mazmuni', db.Text)
    datetime = db.Column('Sana', db.DateTime, default=datetime.now)
    views = db.Column("Ko'rishlar soni", db.Integer, default=0)


if __name__ == "__main__":
    db.create_all()
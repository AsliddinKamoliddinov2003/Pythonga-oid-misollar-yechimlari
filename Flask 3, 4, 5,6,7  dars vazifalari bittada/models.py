from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import app
from slugify import slugify

db = SQLAlchemy(app)

class Category(db.Model):
    id=db.Column('ID', db.Integer,primary_key=True)
    name=db.Column('Kategoriyalar nomi', db.String(255))


class News(db.Model):
    id = db.Column('ID', db.Integer, primary_key = True)
    title = db.Column('Sarlavha', db.String(255))
    slug = db.Column("Slug",db.String(255))
    content = db.Column('Mazmuni', db.Text)
    datetime = db.Column('Sana', db.DateTime, default=datetime.now)
    views = db.Column("Ko'rishlar soni", db.Integer, default=0)
    is_published=db.Column("chop etilishi", db.Boolean)
    photo=db.Column("Muqova rasmi", db.String(255),nullable=True)

    cat_id=db.Column(db.Integer,db.ForeignKey("category.ID"),nullable=True)

    def __init__(self,*args,**kwargs):
        if not "slug" in kwargs:
            kwargs["slug"]=slugify(kwargs['title'])
        super().__init__(*args,**kwargs)
 
# n=News(title="""JCh—2022 yo‘lida. Braziliyadan navbatdagi g‘alaba, Argentina so‘nggi daqiqada galabani qo‘ldan chiqardi. Urugvayda esa durang
# """,content=""" Argentina terma jamoasi Kolumbiya maydonida mehmon bo‘ldi. O‘yin debyutida Kristian Romero va Leandro Paredesning gollaridan keyin mehmonlar oldinga o‘tib oldi. Ikkinchi bo‘lim debyutida Luis Muriel hisobni qisqartirgan bo‘lsa, o‘yin yakunlanishi arafasida Migel Borxa muvozanatni tikladi.

# Braziliya terma jamoasi safarda Paragvay bilan o‘ynadi. Neymar 4-daqiqada hisobni ochdi o‘yin yakunlanishi arafasida Lukas Paketa “pentakampionlar”ning ikkinchi golini urdi.

# Urugvay kutilmaganda Venesuelani yenga olmadi. Chili esa Ekvador bilan durang o‘ynadi.

# Braziliya 6-turdan keyin yuz foizlik natija bilan birinchi o‘rinda ketmoqda. Ikkinchi o‘rindagi Argentinada 12 ochko bor. Ekvador (9), Urugvay va Kolumbiya (8 ochkodan) keyingi pog‘onalarda bormoqda.""")
# db.session.add(n)
# db.session.commit()

if __name__ == "__main__":
    db.create_all()
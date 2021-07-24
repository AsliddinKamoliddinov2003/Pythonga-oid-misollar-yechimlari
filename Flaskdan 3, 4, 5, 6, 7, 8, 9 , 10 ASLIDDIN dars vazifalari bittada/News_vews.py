from config import app
from flask import request,render_template
from models import News,db
from utils.search import highlight_words

@app.route("/")
def all_news_view():
    #cats=Category.query.all()
    term=request.args.get("soz",None)
    cat_id=request.args.get("category",None)

    if term:
        all_news=News.query.filter(News.title.contains(term) | News.content.contains(term)).all()
        temp=[]
        for single_news in all_news:
            single_news.title=highlight_words(single_news.title,term,"<span style='beckground-color: yellow; font-weight: bold; color: black;'>","</span>")

            single_news.content=highlight_words(single_news.content,term,"<span style='beckground-color: yellow; font-weight:bold; color: black;'>","</span>")
            temp.append(single_news)
        all_news=temp
    else:
        all_news=News.query.all()

    if cat_id:
        all_news=News.query.filter_by(cat_id=int(cat_id)).all()
    else:
        all_news=News.query.all()

    return render_template("client/all-news.html", yangiliklar=all_news,qidirilgan_soz=term)

@app.route("/<string:slug>/")
def single_news_view(slug):
    single_news = News.query.filter_by(slug=slug).first_or_404()

    if single_news.views is None:
        single_news.views=0

    single_news.views=single_news.views+1

    db.session.commit()
    return render_template("client/single-news.html", yangilik=single_news)






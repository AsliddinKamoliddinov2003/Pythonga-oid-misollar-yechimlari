from logging import debug
from flask import render_template

from config import app
from models import News

@app.route("/")
def all_news_view():
    all_news = News.query.all()
    return render_template("all-news.html", yangiliklar=all_news)

@app.route("/<int:_id>/")
def single_news_view(_id):
    single_news = News.query.filter_by(id=str(_id)).first_or_404()
    return render_template("single-news.html", yangilik=single_news)


@app.errorhandler(404)
@app.errorhandler(500)
def page_404_view(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)
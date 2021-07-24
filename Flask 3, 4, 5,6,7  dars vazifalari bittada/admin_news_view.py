from flask.templating import render_template
from config  import app
from models import News

@app.route("/admin/news/")
def admin_news_view():
    return render_template("admin/news_list.html")
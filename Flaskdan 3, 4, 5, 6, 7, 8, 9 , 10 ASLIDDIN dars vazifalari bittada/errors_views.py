from config import  app
from flask import render_template


@app.errorhandler(404)
@app.errorhandler(500)
def page_404_view(e):
    return render_template("404.html")
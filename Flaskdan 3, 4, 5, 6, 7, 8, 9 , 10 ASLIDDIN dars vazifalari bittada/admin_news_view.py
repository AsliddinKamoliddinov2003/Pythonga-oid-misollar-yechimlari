from flask import render_template,request,redirect,url_for
from config import app, os_upload_path
from uuid import uuid4
from models import News,Category,db
from slugify.slugify import  slugify
import os

@app.route("/admin/news/")
def admin_news_list_view():
    if ('action' and '_id') in request.args:
        try:
            _id=int(request.args.get("_id"))
        except:
            return redirect("url_for('admin_news_list_view)")

        if request.args.get("action")=="make_active":

            chosen_news=News.query.filter_by(id=_id).first_or_404()
            chosen_news.is_published=True
            db.session.commit()

        elif  request.args.get("action")=="make_inactive":

            chosen_news=News.query.filter_by(id=_id).first_or_404()
            chosen_news.is_published=False
            db.session.commit()

        elif  request.args.get("action")=="delete":

            chosen_news=News.query.filter_by(id=_id).first_or_404()
            news=db.session.delete(chosen_news)
            try:
                os.unlink(os.path.join("static","uploads","images",chosen_news.photo))
            except:
                pass
            db.session.commit()
            return redirect("url_for('admin_news_list_view)")



    all_news=News.query.all()
    return render_template("admin/news_list.html",yangiliklar=all_news)

@app.route("/admin/news/create/",methods=['GET','POST'])
def add_news_view():

    if request.method=="POST":

        news=News()

        news.title=request.form["news_title"]
        news.slug=slugify(news.title)
        news.content=request.form["news_content"]
        news.is_published=bool(request.form.get("publish_status",False))
        try:
            news.cat_id=int(request.form.get('category_id'))
        except:
            return redirect(url_for("add_news_view"))

        if "news_photo" in request.files:
            news_photo=request.files["news_photo"]
            photo_filename=str(uuid4())+"."+ news_photo.filename.split(".")[-1]
            news_photo.save(os.path.join(os_upload_path,photo_filename))

            if news_photo.filename.split(".")[-1]!="":
                news.photo=photo_filename
                


        news_cat=request.form.get("category_id",None)
        if news_cat:
            news.is_published=True
        else:
            news.is_published=False
        db.session.add(news)
        db.session.commit()

        return redirect(url_for('admin_news_list_view'))

    return render_template("admin/add_news.html")

@app.route("/admin/category/create/", methods=["GET","POST"])
def add_category_view():

    category_name=request.form.get("category_name",None)

    if category_name:
        c=Category(name=category_name)
        db.session.add(c)
        db.session.commit()

    return render_template("admin/add_category.html")

@app.route("/admin/news/<int:_id>/",methods=["GET","POST"])
def update_news_view(_id):
    if request.method=="POST":

        news=News.query.filter_by(id=_id).first_or_404()
        
        news.title=request.form["news_title"]
        news.slug=slugify(news.title)
        news.content=request.form["news_content"]
        news.is_published=bool(request.form.get("publish_status",False))

        try:
            news.cat_id=int(request.form.get('category_id'))
        except:
            return redirect(url_for("update_news_view"))

        if "news_photo" in request.files:
            news_photo=request.files["news_photo"]
            photo_filename=str(uuid4())+"."+ news_photo.filename.split(".")[-1]
            news_photo.save(os.path.join(os_upload_path,photo_filename))

            if news_photo.filename.split(".")[-1]!="":
                news.photo=photo_filename
            
        db.session.commit()
        return redirect(url_for("admin_news_list_view"))

    elif request.method=="GET":

        if  request.args.get("action",None)=="delete-thumb":

            chosen_news=News.query.filter_by(id=_id).first_or_404()
            os.unlink(os.path.join("static","uploads","images",chosen_news.photo))
            chosen_news.photo=""
            db.session.commit()

            return redirect(url_for("update_news_view",_id=_id))

    chosen_news=News.query.filter_by(id=_id).first_or_404()
    return render_template("admin/updates_news.html",  yangilik=chosen_news)
   













from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
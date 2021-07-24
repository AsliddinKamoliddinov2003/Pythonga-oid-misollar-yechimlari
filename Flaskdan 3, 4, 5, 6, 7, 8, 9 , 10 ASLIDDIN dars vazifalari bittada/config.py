from flask import Flask
from pathlib import Path
import os

os_upload_path = os.path.join("static","uploads","images")
IMAGE_UPLOAD_DIR = Path(os_upload_path)

if not IMAGE_UPLOAD_DIR.exists():
    os.makedirs(os_upload_path)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
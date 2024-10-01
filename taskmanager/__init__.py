import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

if os.path.exists("env.py"):
    import env # noqa

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(__name__, template_folder=BASE_DIR.joinpath("templates"), static_folder=BASE_DIR.joinpath("static"))
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes # noqa


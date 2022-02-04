from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

dbdir = "sqlite:///"+os.path.abspath(os.getcwd())+"/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

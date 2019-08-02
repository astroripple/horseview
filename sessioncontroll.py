from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_migrate import Migrate, MigrateCommand
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}/jrdb.db".format(os.environ["DB"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

strobj = db.String(80)
baseobj = db.Model
intobj = db.Integer
colobj = db.Column
relobj = db.relationship
fkyobj = db.ForeignKey
bkrobj = db.backref
sesobj = db.session

manager = APIManager(app, flask_sqlalchemy_db=db)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_migrate import Migrate, MigrateCommand
import os
from sqlalchemy import MetaData

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}/jrdb.db".format(os.environ["DB"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

strobj = db.String(80)
baseobj = db.Model
intobj = db.Integer
jsonobj = db.JSON
colobj = db.Column
relobj = db.relationship
fkyobj = db.ForeignKey
bkrobj = db.backref
sesobj = db.session

manager = APIManager(app, flask_sqlalchemy_db=db)

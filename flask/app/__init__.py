from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import views

####################################################
########SQLAlchemy INSTANZ##########################

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
Migrate(app, db)

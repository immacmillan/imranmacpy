from flask import Flask
from config import Config
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(Config)
app.debug=True
mongo = PyMongo(app)

from app import routes
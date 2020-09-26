from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import *
from CovidNER.ner.Text import Text

app = Flask(__name__)

# activate if we need DB
# app.config.from py-file('config.py')
# db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()


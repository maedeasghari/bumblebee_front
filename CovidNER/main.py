from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# activate if we need DB
#app.config.from_pyfile('config.py')
#db = SQLAlchemy(app)

from views import * 
if __name__ == '__main__':
    app.run() 
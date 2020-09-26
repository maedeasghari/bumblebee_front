from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from .views import *
from CovidNER.ner.Text import Text

app = Flask(__name__)

# activate if we need DB
# app.config.from py-file('config.py')
# db = SQLAlchemy(app)

if __name__ == '__main__':
    # app.run()
    color_word_map_dict = {
        'disease': 'red',
        'disease,chemical': 'purple',
        'chemical': 'blue',
        'protein,gene': 'green',
        'cell_type': 'green',
        'dna': 'green',
        'disease,cell_type': 'yellow',
    }
    text = Text('data/in.csv', color_word_map_dict, 'outputs/out.txt')
    text.text_maker(True)


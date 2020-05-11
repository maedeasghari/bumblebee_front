from main import app
from ner import Text

@app.route('/covidner')
def covidner():
    color_word_map_dict = {
    'disease': 'red',
    'disease,chemical': 'purple',
    'chemical': 'blue',
    'protein,gene': 'green',
    'cell_type': 'green',
    'dna': 'green',
    'disease,cell_type': 'yellow',
    }
    text = Text.Text('data/in.csv', color_word_map_dict, 'outputs/out.txt')
    text.text_maker(False)
    template_fh = open('outputs/template.html', 'r')
    template= template_fh.read()
    template = template.replace('#values#' , str(text.text_dict))

    return template
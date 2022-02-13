from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', page_title='Заготовка',
                           some_text='Немного информации о Марсе')


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', page_title='Заготовка', profession=prof)


@app.route('/list_prof/<type_list>')
def list_prof(type_list):
    if type_list in ['ol', 'ul']:
        return render_template('professions_list.html', page_title='Список профессий', type_list=type_list)
    else:
        return 'Неверный параметр'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

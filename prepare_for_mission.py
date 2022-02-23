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


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    params = {
        'title': 'Анкета',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'Выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': True
    }
    return render_template('auto_answer.html', **params)


@app.route('/distribution')
def distribution():
    astronauts = ['Маша', 'Петя', 'Вася', 'Даша']
    return render_template('distribution.html', title='Размещение по каютам', names=astronauts)


@app.route('/table/<string:sex>/<int:age>')
def choose_room(sex, age):
    return render_template('choose_room.html', title='Оформление каюты', sex=sex, age=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

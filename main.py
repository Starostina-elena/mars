from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def start_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():

    text = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]

    return '</br>'.join(text)


@app.route('/image_mars')
def image_mars():

    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
                    alt="здесь должна была быть картинка, но не нашлась" width=200 height=200>
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def add_with_pic():
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
                    alt="здесь должна была быть картинка, но не нашлась" width=200 height=200>
                    </br>
                    </br>
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="ru">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h2>Анкета претендента</h2>
                            <h3>на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <br>
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Общее</option>
                                        </select>
                                     </div>
                                    <br>
                                    <p>Какие у Вас есть профессии?</p>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof1" name="prof1">
                                        <label class="form-check-label" for="prof1">Инженер-исследователь</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof2" name="prof2">
                                        <label class="form-check-label" for="prof2">Инженер-строитель</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof3" name="prof3">
                                        <label class="form-check-label" for="prof3">Пилот</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof4" name="prof4">
                                        <label class="form-check-label" for="prof4">Метеоролог</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof5" name="prof5">
                                        <label class="form-check-label" for="prof5">Инженер по жизнеобеспечению</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof6" name="prof6">
                                        <label class="form-check-label" for="prof6">Инженер по радиационной защите</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof7" name="prof7">
                                        <label class="form-check-label" for="prof7">Врач</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input" id="prof8" name="prof8">
                                        <label class="form-check-label" for="prof8">Экзобиолог</label>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print('Имя:', request.form['name'])
        print('Фамилия:', request.form['surname'])
        print('Почта:', request.form['email'])
        print('Образование:', request.form['education'])
        print('Фото:', request.form['file'])
        print('О себе:', request.form['about'])
        print('Готов остаться:', 'да' if request.form.get('accept') else 'нет')
        print('Пол:', request.form['sex'])
        professions = []
        if request.form.get('prof1'):
            professions.append('Инженер-исследователь')
        if request.form.get('prof2'):
            professions.append('Инженер-строитель')
        if request.form.get('prof3'):
            professions.append('Пилот')
        if request.form.get('prof4'):
            professions.append('Метеоролог')
        if request.form.get('prof5'):
            professions.append('Инженер по жизнеобеспечению')
        if request.form.get('prof6'):
            professions.append('Инженер по радиационной защите')
        if request.form.get('prof7'):
            professions.append('Врач')
        if request.form.get('prof8'):
            professions.append('Экзобиолог')
        print('Профессии:', ', '.join(professions))
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice_planet(planet_name):
    print(type(planet_name))
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {planet_name.capitalize()}</h1>
                    <div class="alert alert-primary" role="alert">
                      Эта планета близка к Земле;
                    </div>
                    <div class="alert alert-success" role="alert">
                      На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-info" role="alert">
                      На ней есть вода и атмосфера;
                    </div>
                    <div class="alert alert-light" role="alert">
                      На ней есть небольшое магнитное поле;
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Наконец, она просто красива!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

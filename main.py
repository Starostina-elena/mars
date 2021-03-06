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


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {level} отбора 
                    </div>
                    <p>Составляет {rating}!</p>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
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
                            <h2>Загрузка фотографии</h2>
                            <h3>для участия в миссии</h3>
                            <div>
                                <form class="load_photo_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-info">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        request.files['file'].save('static/img/user_photo.jpg')
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
                                    <h2>Загрузка фотографии</h2>
                                    <h3>для участия в миссии</h3>
                                    <div>
                                        <form class="load_photo_form" method="post" enctype="multipart/form-data">
                                            <div class="form-group">
                                                <label for="photo">Приложите фотографию</label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>
                                            <br>
                                            <img src="{url_for('static', filename='img/user_photo.jpg')}" 
                                            alt="Похоже, при загрузке картинки что-то пошло не так" width=200 height=200>
                                            <br>
                                            <button type="submit" class="btn btn-info">Отправить</button>
                                        </form>
                                    </div>
                                  </body>
                                </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <script src="https://getbootstrap.com/docs/5.1/dist/js/bootstrap.bundle.min.js"
                    integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
                    crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.js"></script>
                    <script src="https://getbootstrap.com/docs/5.1/assets/js/docs.min.js"></script>
                    <title>Пейзажи Марса</title>
                  </head>
                  <body>
                    <h1 class=formatting_v_2>Пейзажи Марса</h1>
                    <br>
                    <div class="wrapper-carousel">
                        <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                            <div class="carousel-indicators">
                                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                            </div>
                            <div class="carousel-inner">
                                <div class="carousel-item active">
                                    <img src="{url_for('static', filename='img/mars_carousel_1.jpg')}" width=320 height=240
                                    class="d-block w-100" alt="Здесь должна была быть картинка, но не нашлась">
                                </div>
                                <div class="carousel-item">
                                  <img src="{url_for('static', filename='img/mars_carousel_2.jpg')}" width=360 height=225
                                  class="d-block w-100" alt="Здесь должна была быть картинка, но не нашлась">
                                </div>
                                <div class="carousel-item">
                                  <img src="{url_for('static', filename='img/mars_carousel_3.jpg')}" width=341 height=256
                                  class="d-block w-100" alt="Здесь должна была быть картинка, но не нашлась">
                                </div>
                            </div>
                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                            </button>
                        </div>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

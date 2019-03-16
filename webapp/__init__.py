from flask import Flask, render_template

from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city

def create_app():
    app = Flask(__name__) # __name__ - имя текущего файла
    app.config.from_pyfile('config.py')

    @app.route('/') # декоратор
    def index():
        title = 'Новости Python'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = get_python_news()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)

    return app


    #if weather:    
        #weather_text = f"Погода: {weather['temp_C']}, ощущается как: {weather['FeelsLikeC']}"
        #return f"Погода: {weather['temp_C']}, ощущается как: {weather['FeelsLikeC']}"
    #else:
        #weather_text = 'Сервис погоды временно недоступен'
        #return 'Сервис погоды временно недоступен'
from flask import Flask
from flask_moment import moment
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()

def create_app(config_name):
    '''
    Uygulama yapılandırıcısı, uygulama için gerekli eklentiler ekleniyor,
    hangi Congif sınıfı kullanılıyorsa ona göre uygulama oluşturuşuyor.
    '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)

    return app

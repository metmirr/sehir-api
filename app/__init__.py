# -*- coding:utf-8 -*-
from flask import Flask
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import config

# Eklentiler 
db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()

def create_app(config_name):
    '''
    Uygulama yapılandırıcısı, uygulama için gerekli eklentiler ekleniyor,
    hangi Config sınıfı kullanılıyorsa ona göre uygulama oluşturuşuyor.
    '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from app.api_v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

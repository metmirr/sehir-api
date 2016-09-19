# -*- coding:utf-8 -*-
'''
Configurasyon ayarları.
'''
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    '''
    Temel config sınıfı, uygulama ile ilgili temel konfügürasyonlar bu sınıfta
    belirlenir diğer sınıflar ise bundan türeatilir.
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gizli string buraya yazılacak'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    '''
    Geliştirme aşamasında kullanılacak config sınıfı
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev-data.sqlite')

class TestConfig(Config):
    '''
    Test aşamasında kullanılacak config sınıfı
    '''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or\
     'sqlite:///' + os.path.join(basedir, 'test-data.sqlite')

class ProConfig(Config):
    '''
    Projeyı yayınlamada kullanılacak config
    '''
    SQLALCHEMY_POOL_RECYCLE = 200
    SQLALCHEMY_POOL_TIMEOUT = 20
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRO_DATABASE_URL') or\
     'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'dev': DevConfig,
    'test': TestConfig,
    'pro': ProConfig,

    'default': DevConfig
}

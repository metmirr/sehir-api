'''
Configurasyon ayarları.
'''
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gizli string buraya yazılacak'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_POOL_RECYCLE = 200
    SQLALCHEMY_POOL_TIMEOUT = 20

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    '''
    Geliştirme aşamasında kullanılacak config sınıfı
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = os.environ.get('DEV_DATABASE_URL' or\
            'sqlite:///' + os.path.join(basedir, 'dev-data.sqlite')

class TestConfig(Config):
    '''
    Testler için kullanılacak config sınıfı
    '''
    TESTING = True
    SQLALCHEMY_DATABASE_URL = os.environ.get('TEST_DATABASE_URL') or\
            'sqlite:///' + os.path.join(basedir, 'test-data.sqlite')
class ProConfig(Config):
    '''
    Projeyı yayınlamada kullanılacak config
    '''
    SQLALCHEMY_DATABASE_URL = os.environ.get('PRO_DATABASE_URL') or\
            'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'dev': DevConfig,
    'test': TestConfig,
    'pro': ProConfig,

    'default': DevConfig
}

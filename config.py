
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'chatapp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    port = 8888


class DevConfig(BaseConfig):
    port = 8000
    DEBUG = True
    TESTING = False
    ENV = 'Dev'
    APPNAME = 'Chatapp'
    SQLALCHEMY_ECHO = True


class ProdConfig(BaseConfig):
    port = 8000
    DEBUG = True
    TESTING = False
    ENV = 'Prod'
    APPNAME = 'Chatapp'
    SQLALCHEMY_ECHO = True

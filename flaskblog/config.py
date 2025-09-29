import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # We need a secret key, will protect our app
    # CDM>python>import secrets>secrets.toker_hex(16)
    SECRET_KEY = os.getenv('SECRET_KEY', '53276704145fa42c0afb6ee4fdfaf9b4')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'site.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
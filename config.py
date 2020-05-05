import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:eagle@127.0.0.1:5432/db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/gestion_celulares'
SQLALCHEMY_TRACK_MODIFICATIONS = False

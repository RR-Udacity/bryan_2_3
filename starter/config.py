import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'server-west.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'database-west'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'bryan'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Hornet38!'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'storageaccoutn123253524'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'PApN+M7a3F6FliRiBZgOv+jMz67OaEyagj6vTcoXBlai56pidXlM/Ni458vsEuUw0hTasf5Q8qkcR6rX5o53Mg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
import os

# print(os.environ.get('SECRET_KEY'))
# print(os.environ.get('BLOB_ACCOUNT'))
# print(os.environ.get('BLOB_STORAGE_KEY'))
# print(os.environ.get('BLOB_CONTAINER'))
# print(os.environ.get('SQL_SERVER'))
# print(os.environ.get('SQL_DATABASE'))
# print(os.environ.get('SQL_USER_NAME'))
# print(os.environ.get('SQL_PASSWORD'))
# print(os.environ.get('CLIENT_SECRET'))
# print(os.environ.get('CLIENT_ID'))

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views

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

print(os.environ.get('SECRET_KEY'))
print(os.environ.get('BLOB_ACCOUNT'))
print(os.environ.get('BLOB_STORAGE_KEY'))
print(os.environ.get('BLOB_CONTAINER'))
print(os.environ.get('SQL_SERVER'))
print(os.environ.get('SQL_DATABASE'))
print(os.environ.get('SQL_USER_NAME'))
print(os.environ.get('SQL_PASSWORD'))
print(os.environ.get('CLIENT_SECRET'))
print(os.environ.get('CLIENT_ID'))

app = Flask(__name__)

app.logger.setLevel(logging.WARNING)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler)

app.logger.info(f'SECRET KEY: {os.environ.get('SECRET_KEY')}')
app.logger.info(f'BLOB ACCOUNT: {os.environ.get('BLOB_ACCOUNT')}')
app.logger.info(f'BLOB STORAGE KEY: {os.environ.get('BLOB_STORAGE_KEY')}')  
app.logger.info(f'BLOB CONTAINER: {os.environ.get('BLOB_CONTAINER')}')
app.logger.info(f'SQL SERVER: {os.environ.get('SQL_SERVER')}') 
app.logger.info(f'SQL DATABASE: {os.environ.get('SQL_DATABASE')}')
app.logger.info(f'SQL USER NAME: {os.environ.get('SQL_USER_NAME')}')
app.logger.info(f'SQL PASSWORD: {os.environ.get('SQL_PASSWORD')}')
app.logger.info(f'CLIENT SECRET: {os.environ.get('CLIENT_SECRET')}')
app.logger.info(f'CLIENT ID: {os.environ.get('CLIENT_ID')}')


app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
# app.logger.setLevel(logging.WARNING)
# streamHandler = logging.StreamHandler()
# streamHandler.setLevel(logging.WARNING)
# app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views

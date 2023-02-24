from flask import Flask                                     # Flask
from flask_restful import Api, Resource, reqparse           # Дополнения к Flask для создания API
import sqlite3                                              # Библиотека для работы с БД


app = Flask(__name__)
api = Api(app)                                              # Создаём приложение и API

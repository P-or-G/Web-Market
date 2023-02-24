from flask import Flask                             # Импорт Flask (приложение для API)
from flask_restful import Api, Resource, reqparse   # Импорт надстроек для Flask для создания API
import sqlite3                                      # Для работы с базой данных


app = Flask(__name__)
api = Api(app)

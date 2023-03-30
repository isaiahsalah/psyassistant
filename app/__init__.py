"""

Este módulo contiene la función para crear la API.

"""
from flask import Flask
from config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


from app import routes
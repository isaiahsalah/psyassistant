import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """olas"""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    API_KEY_GPT = os.environ.get('API_KEY_GPT') or 'No existe'
    API_KEY_WHATS = os.environ.get('API_KEY_WHATS') or 'No existe'
    VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN') or 'No existe'
    MONGO_URI = os.environ.get('MONGO_URI') or 'No existe'


class DevelopmentConfig(Config):
    """olas"""
    DEBUG = True


class ProductionConfig(Config):
    """olas"""
    DEBUG = False

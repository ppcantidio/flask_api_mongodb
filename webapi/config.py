import os
import string
import random


gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for i in range(12))

class Config():
    SECRET_KEY = key
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
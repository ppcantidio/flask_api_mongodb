from flask import Flask
from dotenv import load_dotenv
from webapi.config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

from webapi.controllers.users import users_routes
app.register_blueprint(users_routes, url_prefix='/api/v1/users')

from webapi.controllers.errors import errors_routes
app.register_blueprint(errors_routes)
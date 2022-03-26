import imp
from flask import Blueprint
from webapi.utils import auth


login_routes = Blueprint('login_routes', __name__)

@login_routes.route('/', methods=['POST'])
def login():
    return auth.auth()
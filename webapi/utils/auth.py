import jwt
import datetime
from webapi.app import app
from functools import wraps
from flask import jsonify, request
from webapi.utils.database import Database
from webapi.utils.exceptions import SecurityError
from werkzeug.security import check_password_hash


db = Database()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            raise SecurityError()

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = db.select_one_object('users', {'username': data['username']})
        except:
            return jsonify({
                'status': 'error',
                'message': 'invalid token'
            }), 403
        
        return f(user, *args, **kwargs)
    return decorated

def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        raise SecurityError()

    user  = db.select_one_object('users', {'username': auth.username})

    if not user:
        raise SecurityError()

    if user and check_password_hash(user['password'], auth.password):
        token = jwt.encode({
            'username': user['username'],
            'exp': datetime.datetime.now() + datetime.timedelta(hours=12)
        }, app.config['SECRET_KEY'])

        return jsonify({
            'message': 'Validated sucessfully',
            'token': token.decode('UTF-8'),
            'exp': datetime.datetime.now() +datetime.timedelta(hours=12)
        })

    raise SecurityError()

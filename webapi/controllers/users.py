from bson.objectid import ObjectId
from webapi.utils.database import Database
from webapi.models.users import UsersModels
from webapi.utils import auth
from flask import Blueprint, jsonify, request
from webapi.utils.exceptions import ValidationError


users_routes = Blueprint('users_rotes', __name__)
db = Database()

class UsersRoutes:

    @users_routes.route('/', methods=['POST'])
    def create_user():
        new_user = UsersModels(
            username=request.form.get('username'),
            name=request.form.get('name'),
            email=request.form.get('email'),
            password=request.form.get('password')
        )

        new_user.create_user()

        return jsonify({
            'status': 'success',
            'message': 'success creating user'
        })

    @users_routes.route('/', methods=['GET'])
    def get_users():
        users = db.select_object('users', {})
        
        users_list = []
        for user in users:
            del user['password']
            user['_id'] = str(user['_id'])
            users_list.append(user)

        return jsonify({
            'status': 'success',
            'message': 'success finding users',
            'users': users_list
        })

    @users_routes.route('/<id>', methods=['GET'])
    def get_user(id):
        pass

    @users_routes.route('/<id>', methods=['PUT'])
    def edit_user(id):
        user_doc = db.select_one_object('users', {'_id': ObjectId(id)})

        username = request.form.get('username')
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if username is not None:
            if db.select_one_object('users', {'username': username}) is not None:
                raise ValidationError('there is already a user with that username')
            user_doc['username'] = username

        if name is not None:
            user_doc['name'] = name

        if email is not None:
            if db.select_one_object('users', {'email': email}) is not None:
                raise ValidationError('there is already a user with that username')
            user_doc['email'] = email

        if password is not None:
            user_doc['password'] = password

        user = UsersModels(
            username=user_doc['username'],
            name=user_doc['name'],
            email=user_doc['email'],
            password=user_doc['password'],
        )

        user.update_user(id)

        return jsonify({
            'status': 'success',
            'message': 'successful editing user',
        })

    @users_routes.route('/<id>', methods=['DELETE'])
    def delete_user(id):
        pass

    @users_routes.route('/profile', methods=['GET'])
    @auth.token_required
    def profile(user):
        user['_id'] = str(user['_id'])
        del user['password']
        return jsonify({
            'status': 'success',
            'message': '',
            'user': user
        })
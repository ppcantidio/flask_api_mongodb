from flask import Blueprint


users_routes = Blueprint('users_rotes', __name__)

class UsersRoutes:

    @users_routes.route('/', methods=['POST'])
    def create_user():
        pass

    @users_routes.route('/', methods=['GET'])
    def get_users():
        pass

    @users_routes.route('/<id>', methods=['GET'])
    def get_user(id):
        pass

    @users_routes.route('/<id>', methods=['PUT'])
    def edit_user(id):
        pass

    @users_routes.route('/<id>', methods=['PUT'])
    def delete_user(id):
        pass

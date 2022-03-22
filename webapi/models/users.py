from bson.objectid import ObjectId
from webapi.utils.database import Database
from webapi.utils.exceptions import ValidationError
from werkzeug.security import generate_password_hash


db = Database()

class UsersModels:

    def __init__(self, name, email, password, username):
        self.name = name
        self.email = self.validation_email(email)
        self.password = self.validation_password(password)
        self.username = self.validation_username(username)

    def validation_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must contain more than 8 characters")

        if not any(c.isupper() for c in value):
            raise ValidationError("Password must contain at least one uppercase character")

        if not any(c.islower() for c in value):
            raise ValidationError("Password must contain at least one lowercase character")

        return value

    def validation_username(self, value):
        if len(value) > 10:
            raise ValidationError("The username must contain a maximum of 10 characters")

        return value

    def validation_email(self, value):
        if len(value) > 320:
            raise ValidationError("The email must contain a maximum of 320 characters")

        return value
 
    def create_user(self):
        if db.select_one_object('users', {'username': self.username}) is not None:
            raise ValidationError('there is already a user with that username')

        if db.select_one_object('users', {'email': self.email}) is not None:
            raise ValidationError('there is already a user with that email')

        user_doc = {
            'username': self.username,
            'name': self.name,
            'email': self.email,
            'password': generate_password_hash(self.password)
        }

        db.insert_object(object_dictionary=user_doc, collection='users')

    def update_user(self, id):
        user_doc = {
            'username': self.username,
            'name': self.name,
            'email': self.email,
            'password': generate_password_hash(self.password)
        }

        db.update_object(user_doc, 'users', {'_id': ObjectId(id)})

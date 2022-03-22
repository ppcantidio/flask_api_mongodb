from flask import Blueprint, jsonify
from webapi.utils.exceptions import ValidationError


errors_routes = Blueprint('errors_routes', __name__)

@errors_routes.app_errorhandler(ValidationError)
def handle_validation_error(erro):

    return {
        "status": "error",
        "message": erro.message
        }, 422

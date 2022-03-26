from flask import Blueprint, jsonify
from webapi.utils.exceptions import ValidationError, SecurityError


errors_routes = Blueprint('errors_routes', __name__)

@errors_routes.app_errorhandler(ValidationError)
def handle_validation_error(erro):

    return {
        "status": "error",
        "message": erro.message
        }, 422

@errors_routes.app_errorhandler(SecurityError)
def handle_validation_error(erro):

    return {
        "status": "error",
        "message": 'security error'
        }, 422

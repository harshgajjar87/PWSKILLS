from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return "This is the Login Page"

@auth_bp.route('/register')
def register():
    return "This is the Register Page"
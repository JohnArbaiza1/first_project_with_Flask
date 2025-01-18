from flask import Blueprint
from flask import render_template

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/register')
def register():
    return 'Registro de usuarios'

@auth.route('/login')
def login():
    return render_template('login.html')
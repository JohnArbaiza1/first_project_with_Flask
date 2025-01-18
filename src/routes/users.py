from flask import render_template
from flask import Blueprint

users = Blueprint('users', __name__)

@users.route("/")
def home():
    return render_template('index.html')

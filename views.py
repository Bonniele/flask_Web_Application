
from flask import Blueprint

x = Blueprint('home',__name__)
y = Blueprint('statistics',__name__)

@x.route("/")
def home():
    return " Hello "

@y.route('/statistics')
def statistics():
    return " Welcome to Statistics"
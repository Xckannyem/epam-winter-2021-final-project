from flask import Blueprint
from flask import render_template

user = Blueprint('user', __name__)

from . import auth


@user.route('/')
@user.route('/home')
def home_page():
    """
    Render the home page template on the / route
    """
    return render_template('home.html')

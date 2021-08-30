from flask import render_template, Blueprint
from flask_simplelogin import login_required, get_username
from backend_modules.db_manage.data_access_db import DAO

application_routing = Blueprint("name_configure", __name__)


@application_routing.route('/login')
def login():
    return render_template('login.html')


@application_routing.route('/')
@application_routing.route('/index')
@login_required()
def index():
    db = DAO(get_username())
    user_data = db.get_user_by_login(get_username())
    user_data.pop('password')
    return render_template('index.html', user=user_data)

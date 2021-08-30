from flask_simplelogin import SimpleLogin
from hashlib import sha256
from backend_modules.db_manage.data_access_db import DAO


def atmosphere_login(application_atmosphere):
    def validate_login(user):
        try:
            dao = DAO(user['username'])
            db_user = dao.get_user_by_login(user['username'])
        except:
            return False
        stored_password = db_user['password']
        if stored_password == sha256(user['password'].encode('utf-8')).hexdigest():
            return True
        elif sha256(stored_password.encode('utf-8')).hexdigest() == user['password']:
            return True
        else:
            return False

    SimpleLogin(application_atmosphere, login_checker=validate_login, messages={
        'login_success': 'Вы успешно вошли',
        'login_failure': 'Неверный логин или пароль',
        'is_logged_in': 'Вы уже вошли',
        'logout': 'Вы успешно вышли',
        'login_required': 'Чтобы войти в систему, пожалуйста авторизируйтесь',
        'access_denied': 'Доступ запрещен',
        'auth_error': 'Ошибка аутентификации',
    })

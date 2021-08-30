import copy
import datetime
from backend_modules.db_manage.db import DB


class DAO(object):

    def __init__(self, username=None, user_id=None):
        if username is not None:
            try:
                self.user_id = self.get_user_id(username)
            except:
                self.user_id = user_id
        else:
            if user_id is not None:
                self.user_id = user_id
            else:
                self.user_id = -1  # anonymous

    @staticmethod
    def get_user_id(username):
        return DB().execute(
            sql="""
                        SELECT id FROM users WHERE login=%s 
                    """,
            values=(username,)
        )[0]['id']

    @staticmethod
    def get_user_by_login(login):
        return DB().execute(
            sql="""
                SELECT * FROM users WHERE login=%s
                """,
            values=(login,)
        )[0]

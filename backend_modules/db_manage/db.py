import psycopg2
from contextlib import closing
from psycopg2 import extras


class DB(object):

    def __init__(self):
        # data-string for connect db
        self.dsn = """
        dbname='DBNAME' user='DBUSER' password='DBUSERPASSWORD' host='DBETHADDRESS'
        """

    def get_connect(self):
        return psycopg2.connect(self.dsn)

    def __execute_sql(self, sql, values=tuple()):
        """
        Args:
            sql:
            values:
        """
        conn = None
        if values is None:
            values = tuple()
        result = []

        with closing(psycopg2.connect(self.dsn)) as conn:
            with conn.cursor(cursor_factory=extras.DictCursor) as cursor:
                cursor.execute(sql, values)
                try:
                    result = [dict((cursor.description[i][0], value) \
                                   for i, value in enumerate(row)) for row in cursor.fetchall()]
                except psycopg2.Error:
                    pass
                conn.commit()
        return result

    def execute(self, sql, values=None):
        """
        Args:
            sql:
            values:
        """
        return self.__execute_sql(sql, values)

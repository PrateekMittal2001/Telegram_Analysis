import pymysql


class Database:
    def __init__(self, user, password, host, port, db_name):
        """ Initialize the connection and create the cursor object """
        self._conn = pymysql.connect(user=user, password=password, host=host, port=port, database=db_name)
        self._cursor = self._conn.cursor()

    @property
    def cursor(self):
        """ Return the cursor object """
        return self._cursor

    def execute_query(self, query):
        """ Execute the query """
        self.cursor.execute(query)
        self._conn.commit()

    def fetchall(self, query):
        """ Execute the query and fetch all data """
        self.execute_query(query=query)
        return self.cursor.fetchall()

    def commit(self):
        """ Commit the changes """
        self._conn.commit()
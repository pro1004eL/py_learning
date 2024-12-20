

from abc import ABC, abstractmethod


class DBCursor(ABC): # class for working with DB

    def __init__(self, db_connector):
        self.conn = db_connector

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass # send query to db

    @abstractmethod
    def get_user_filter(self, filter_name, filter_value, filter_sign):
        pass # send query to db


class PostgresDBCursor(DBCursor):
    def get_user_by_id(self, user_id):
        query = ''
        return self.conn.execute(query).fatchall()

    def get_user_filter(self, filter_name, filter_value, filter_sign):
        query = ''
        return self.conn.execute(query).fatchall()


class SqlLiteDBCursor():
    def get_user_by_id(self, user_id):
        query = ''
        return self.conn.execute(query).fatchall()

    def get_user_filter(self, filter_name, filter_value, filter_sign):
        query = ''
        return self.conn.execute(query).fatchall()

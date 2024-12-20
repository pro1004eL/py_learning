

from abc import ABC, abstractmethod


class DBCursor:

    def __init__(self, db_connector):
        self.conn = db_connector

    def get_user_by_id(self, user_id):
        pass # send query to db
    def get_user_filter(self, filter_name, filter_value, filter_sign):
        pass # send query to db

print(isinstance('name', str))
print(isinstance(5, int))
print(isinstance(True, bool))
print(isinstance(True, dict))
print(type(None))




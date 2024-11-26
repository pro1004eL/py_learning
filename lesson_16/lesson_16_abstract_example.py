

from abc import ABC, abstractmethod


class DBCursor:

    def __init__(self, db_connector):
        self.conn = db_connector

    def get_user_by_id(self):
        pass # send query to db
    def get_user_filter(self, filter_name, filter_value, filter_sign):
        pass # send query to db




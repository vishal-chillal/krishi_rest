from django.db import models


class DB(object):
    """docstring for DB"""

    def __init__(self):
        self.create_con()

    def create_con(self):
        print models.Model


db = DB()

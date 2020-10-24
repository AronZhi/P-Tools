import sqlite3
from .DBConnection import *

class Sqlite3Connection(DBConnection):
    def __init__(self, db):
        DBConnection.__init__(self)
        self.connection = sqlite3.connect(db)

    def __del__(self):
        if self.connection:
            self.connection.close()

    def Query(self, command):
        if not self.connection:
            return None
        data = self.connection.execute(command)
        return data

    def Execute(self, command):
        if not self.connection:
            return
        self.connection.execute(command)

    def Commit(self):
        if not self.connection:
            return
        self.connection.commit()
    
    def Close(self):
        if not self.connection:
            return
        self.connection.close()
        self.connection = None
            
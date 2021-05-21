import sqlite3
from DBObj import *

class Sqlite3Obj(DBObj):
    def __init__(self, config):
        super().__init__(config)
        self.connection = sqlite3.connect(config)
    
    def __del__(self):
        if self.connection:
            self.connection.close()
        
    def Close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def GetConnection(self)->sqlite3.Connection:
        return self.connection
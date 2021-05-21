import pymysql
from DBObj import *

class MySqlObj(DBObj):
    def __init__(self, config):
        super().__init__(config)
        self.connection = pymysql.Connect(**config)
    
    def __del__(self):
        if self.connection:
            self.connection.close()
        
    def Close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def GetConnection(self)->pymysql.Connection:
        return self.connection
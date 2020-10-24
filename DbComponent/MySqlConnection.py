import pymysql
from .DBConnection import *

class MySqlConnection(DBConnection):
    def __init__(self, userName, password, hostIP, dbName):
        DBConnection.__init__(self)
        self.connection = pymysql.connect(host=hostIP, user=userName, passwd=password, db=dbName)

    def __del__(self):
        if self.connection:
            self.connection.close()
    
    def Query(self, command):
        if not self.connection:
            return None
        cur = self.connection.cursor()
        cur.execute(command)
        ret = cur.fetchall()
        cur.close()
        return ret
    
    def Execute(self, command):
        if not self.connection:
            return
        cur = self.connection.cursor()
        cur.execute(command)
        cur.close()

    def Close(self):
        if not self.connection:
            return
        self.connection.close()
        self.connection = None
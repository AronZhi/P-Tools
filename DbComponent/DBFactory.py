import sqlite3
from .MySqlConnection import *
from .Sqlite3Connection import *


class DBFactory(object):
    def CreateMySql(self, userName, password, hostIP, dbName):
        return MySqlConnection(userName, password, hostIP, dbName)
    
    def CreateSqlite3(self, dbFile):
        return Sqlite3Connection(dbFile)
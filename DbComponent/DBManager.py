import pymysql
import sqlite3
from .DBFactory import *
from .DBConnection import *

class DBManager(object):
    def __init__(self):
        self.mySqlMap = dict()
        self.sqlite3Map = dict()
        self.factory = DBFactory()
    
    def __del__(self):
        for _, mySqlconn in self.mySqlMap.items:
            mySqlconn.Close()
        for _, sqlite3Conn in self.sqlite3Map.items():
            sqlite3Conn.Close()
    
    def AddMySql(self, userName, password, hostIP, dbName):
        if self.mySqlMap.get(dbName, None):
            self.mySqlMap[dbname].Close()
        self.mySqlMap[dbname] = self.factory.CreateMySql(userName, password, hostIP, dbName)
    
    def GetMysql(self, dbName)->DBConnection:
        return self.mySqlMap.get(dbName, None)

    def DelMysql(self, dbName):
        if self.mySqlMap.get(dbFile, None):
            conn = self.mySqlMap.pop(dbName)
            conn.Close()
    
    def AddSqlite3(self, dbFile):
        if self.sqlite3Map.get(dbFile, None):
            self.sqlite3Map[dbFile].Close()
        self.sqlite3Map[dbFile] = self.factory.CreateSqlite3(dbFile)
    
    def GetSqlite3(self, dbFile)->DBConnection:
        return self.sqlite3Map.get(dbFile, None)

    def DelSqlite3(self, dbFile):
        if self.sqlite3Map.get(dbFile, None):
            conn = self.sqlite3Map.pop(dbFile)
            conn.Close()
    
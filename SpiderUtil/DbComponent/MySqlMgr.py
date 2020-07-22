import pymysql
from DbComponent.Singleton import *


class DBConnection(object):
    def __init__(self, username = '', password = '', host = '', db = ''):
        self.username = username
        self.password = password
        self.host = host
        self.db = db
        self.connection = None


    def __del__(self):
        if self.connection:
            self.connection.close()


    def __repr__ (self):
        return 'db:%s, host:%s, user:%s' %(self.db, self.host, self.username)


    def __str__ (self):
        return 'db:%s, host:%s, user:%s' %(self.db, self.host, self.username)


    def Query(self, sql):
        if self.connection:
            cur = self.connection.cursor()
            cur.execute(sql)
            ret = cur.fetchall()
            cur.close()
            return ret
        return None

    
    def Execute(self, sql):
        if self.connection:
            cur = self.connection.cursor()
            cur.execute(sql)
            cur.close()


@singleton
class MySqlMgr(object):
    def __init__(self):
        self.DBmap = {}

    
    def __del__(self):
        for db in self.DBmap:
            if self.DBmap[db].connection:
                self.DBmap[db].connection.close()
                self.DBmap[db].connection = None


    def SetDBConnectInfo(self, db, username, password, host):
        dbConnInfo = DBConnection(username, password, host, db)
        self.DBmap[db] = dbConnInfo


    def Connect(self, db):
        dbConnInfo = self.DBmap.get(db, None)
        if dbConnInfo is None:
            return False
        
        if dbConnInfo.connection:
            return False
        
        dbConnInfo.connection = pymysql.connect(host=dbConnInfo.host, user=dbConnInfo.username, passwd=dbConnInfo.password, db=db)
        return True
    

    def GetDB(self, db):
        dbConnInfo = self.DBmap.get(db, None)
        return dbConnInfo


g_mysql_mgr = MySqlMgr()
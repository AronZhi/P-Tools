import pymysql
from Decorator.Singleton import *


class MySqlConnection(object):
    def __init__(self, username, password, host, db):
        self.username = username
        self.password = password
        self.host = host
        self.db = db
        self.connection = pymysql.connect(host=host, user=username, passwd=password, db=db)


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

    
    def Close(self):
        if self.connection:
            self.connection.close()
            self.connection = None


@singleton
class MySqlMgr(object):
    def __init__(self):
        self.DBmap = dict()

    
    def __del__(self):
        for db in self.DBmap:
            self.DBmap[db].Close()


    def GenerateDB(self, db, username, password, host):
        if self.DBmap.get(db, None) is None:
            self.DBmap[db] = MySqlConnection(username, password, host, db)
        return self.DBmap[db]
    

    def GetDB(self, db)->MySqlConnection:
        return self.DBmap.get(db, None)


g_mysql_mgr = MySqlMgr()
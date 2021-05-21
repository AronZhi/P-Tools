from DBObj import *

class DBMgr(object):
    def __init__(self) -> None:
        self.DBObjMap = {}
    
    def __del__(self):
        for db in self.DBObjMap:
            db.Close()
    
    def AddDB(self, name, db: DBObj):
        old = self.DBObjMap.get(name, None)
        if old:
            old.Close()
        self.DBObjMap[name] = db
    
    def GetDBConnection(self, name):
        obj = self.DBObjMap.get(name, None)
        if obj:
            return obj.GetConnection()
        return None
    
    def GetDB(self, name):
        return self.DBObjMap.get(name, None)
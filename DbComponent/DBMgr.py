import pymysql
from influxdb import InfluxDBClient

class DBMgr(object):
    def __init__(self) -> None:
        self.mysqlMap = map()
        self.influxdbMap = map()
    
    def __del__(self):
        for db in self.mysqlMap:
            db.close()
        for db in self.influxdbMap:
            db.close()

    def AddMySql(self, config):
        connection =  pymysql.Connect(**config)
        db = self.mysqlMap.get(config["db"], None)
        if db:
            db.close()
        self.mysqlMap[config["db"]]= connection
    
    def GetMysql(self, db: str)->pymysql.Connection:
        return self.mysqlMap.get(db, None)
    
    def AddInfluxDB(self, config):
        connection = InfluxDBClient(**config)
        db = self.mysqlMap.get(config["database"], None)
        if db:
            db.close()
        self.influxdbMap[config["database"]]= connection
    
    def GetInfluxDB(self, db: str)->InfluxDBClient:
        return self.influxdbMap.get(db, None)
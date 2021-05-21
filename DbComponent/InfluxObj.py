from influxdb import InfluxDBClient
from DBObj import *

class Influx(DBObj):
    def __init__(self, config):
        super().__init__(config)
        self.connection = InfluxDBClient(**config)
    
    def __del__(self):
        if self.connection:
            self.connection.close()
        
    def Close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def GetConnection(self)->InfluxDBClient:
        return self.connection
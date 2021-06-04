from Config import Config

class ConfigMgr(object):
    def __init__(self) -> None:
        self.configMap = {}
    
    def getConfig(self, label):
        return self.configMap.get(label, None)
    
    def addConfig(self, label, path):
        self.configMap[label] = Config(path)

g_configMgr = ConfigMgr()
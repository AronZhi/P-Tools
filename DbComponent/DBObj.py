class DBObj(object):
    def __init__(self, config):
        self.connection = None
    
    def Close(self):
        pass

    def GetConnection(self):
        return None
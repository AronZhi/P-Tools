import os

class BaseChart(object):
    def __init__(self):
        self.data = None
        self.show = True
        self.save = False
        self.output = ''
    
    def HandleData(self, data):
        """
        设置数据
        """
        self.data = data
    
    def SetParam(self, **kwargs):
        self.show = kwargs.get('show', True)
        self.save = kwargs.get('save', False)
        if self.save:
            self.output = kwargs.get('output', os.path.join(os.getcwd(), 'chart.png'))

    def Generate(self):
        pass
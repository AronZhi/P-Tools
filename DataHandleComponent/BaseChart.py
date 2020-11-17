import json
import pandas
import matplotlib
from pylab import mpl

class BaseChart(object):
    def __init__(self):
        self.data = None
        self.frame: pandas.DataFrame = None
        self.show = False
        self.save = False
    
    def SetData(self, data):
        self.data = data
    
    def HandleData(self, **kwargs):
        self.frame = pandas.DataFrame(self.data)

    def Generate(self):
        pass

    def _PyLabChinse(self):
        mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
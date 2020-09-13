import numpy
import pandas
import matplotlib
import sqlite3
from pylab import mpl

class ChartKind(object):
    Line = 'line'


class Chart(object):
    def __init__(self):
        self.dataFrame: pandas.DataFrame = None

    
    def SetData(self, data: pandas.DataFrame):
        self.dataFrame = data


    def SetChineseFont(self):
        mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
        

    def Generate(self, x_axis, y_axis, char_kind = ChartKind.Line, **args):
        isGrid = args.get('grid', False)
        isShow = args.get('show', False)
        
        self.dataFrame.plot(x = x_axis, y = y_axis, kind = char_kind, grid = isGrid)
        if isShow:
            matplotlib.pyplot.show()
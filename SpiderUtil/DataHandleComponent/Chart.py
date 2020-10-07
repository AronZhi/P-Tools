import numpy
import pandas
import seaborn
import matplotlib
import sqlite3
from pylab import mpl


class Chart(object):
    def __init__(self):
        self.dataFrame: pandas.DataFrame = None

    
    def SetData(self, data: pandas.DataFrame):
        self.dataFrame = data


    def SetChineseFont(self):
        mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
        

    def GenerateLine(self, x_axis, y_axis, **args):
        self.dataFrame.plot.line(x = x_axis, y = y_axis, grid = args.get('grid', False))
        if args.get('title', None):
            matplotlib.pyplot.title(args['title'])
        if args.get('show', False):
            matplotlib.pyplot.show()

    
    def GenerateBar(self, x_axis, y_axis, **args):
        self.dataFrame.plot.bar(x = x_axis, y = y_axis, grid = args.get('grid', False))
        if args.get('title', None):
            matplotlib.pyplot.title(args['title'])
        if args.get('show', False):
            matplotlib.pyplot.show()

    
    def GenerateBath(self, x_axis, y_axis, **args):
        self.dataFrame.plot.barh(x = x_axis, y = y_axis, grid = args.get('grid', False))
        if args.get('title', None):
            matplotlib.pyplot.title(args['title'])
        if args.get('show', False):
            matplotlib.pyplot.show()


    def GenerateHistogram(self, x_axis, y_axis, **args):
        self.dataFrame.plot.hist(x = x_axis, y = y_axis, grid = args.get('grid', False))
        if args.get('title', None):
            matplotlib.pyplot.title(args['title'])
        if args.get('show', False):
            matplotlib.pyplot.show()

    
    def GenerateDensity(self, **args):
        seaborn.distplot(self.dataFrame, bins=100, color='k')
        if args.get('title', None):
            matplotlib.pyplot.title(args['title'])
        if args.get('show', False):
            matplotlib.pyplot.show()

    
    def GeneratePie(self, **args):
        size = self.dataFrame.values
        labels = self.dataFrame.index
        self.dataFrame.plot.pie(y=labels, autopct='%1.1f%%',shadow=False)
        if args.get('title', None):
            matplotlib.pyplot.title(args['title'])
        if args.get('show', False):
            matplotlib.pyplot.show()
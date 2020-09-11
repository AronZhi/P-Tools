import numpy
import pandas
import matplotlib
import sqlite3
from pylab import mpl

class Chart(object):
    def __init__(self):
        self.dataFrame: pandas.DataFrame = None
        pass


    def SetCsvData(self, csvFile, colum: list = None):
        if colum:
            self.dataFrame = pandas.read_csv(csvFile, names = colum)
        else:
            self.dataFrame = pandas.read_csv(csvFile)


    def SetSqliteData(self, db, sql):
        with sqlite3.connect(db) as conn:
            self.dataFrame = pandas.read_sql_query(sql, conn)
        return

    
    def SetData(self, data: pandas.DataFrame):
        self.dataFrame = data


    def SetChineseFont(self):
        mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
        
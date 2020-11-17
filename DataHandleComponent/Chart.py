import matplotlib
from pylab import mpl
from .BaseChart import *

class Chart(BaseChart):
    def __init__(self):
        BaseChart.__init__(self)
    
    def _PyLabChinse(self):
        mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
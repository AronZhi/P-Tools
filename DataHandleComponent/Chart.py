import matplotlib
from pylab import mpl
from .BaseChart import *

class Chart(BaseChart):
    def __init__(self):
        BaseChart.__init__(self)
    
    def _PyLabChinse(self):
        mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

class RectangularCoordinateChart(Chart):
    def __init__(self):
        Chart.__init__(self)
        self.grid = False
        self.title = ''
    
    def SetParam(self, **kwargs):
        """
        x_axis: x轴, 必须设置
        y_axis: y轴，必须设置
        show: 是否显示生成的图片
        chinse: 数据中是否包含中文,如果包含中文必须设置为True
        save: 是否保存生成图片
        output: 图片保存路径，默认当前路径
        grid: 是否显示网格
        title: 图表标题
        """
        Chart.SetParam(self)
        self.x = kwargs.get('x_axis', None)
        assert self.x
        self.y = kwargs.get('y_axis', None)
        assert self.y
        if kwargs.get('chinse', False):
            self._PyLabChinse()
        self.grid = kwargs.get('grid', False)
        self.title = kwargs.get('title', 'RectangularCoordinateChart')
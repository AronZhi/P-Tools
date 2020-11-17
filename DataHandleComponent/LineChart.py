from .BaseChart import *

class LineChart(BaseChart):
    def __init__(self):
        BaseChart.__init__(self)
        
    def HandleData(self, **kwargs):
        """
        x_axis: x轴, 必须设置
        y_axis: y轴，必须设置
        show: 是否显示生成的图片
        chinse: 数据中是否包含中文
        """
        self.x = kwargs.get('x_axis', None)
        assert self.x
        self.y = kwargs.get('y_axis', None)
        assert self.y
        self.grid = kwargs.get('grid', False)
        self.show = kwargs.get('show', True)
        self.frame = pandas.DataFrame(self.data)
        if kwargs.get('chinse', False):
            self._PyLabChinse()

    def Generate(self):
        if self.x and self.y:
            self.frame.plot.line(x = self.x, y = self.y, grid = self.grid)
            if self.show:
                matplotlib.pyplot.show()
            return True
        else:
            return False
from .Chart import *

class LineChart(Chart):
    def __init__(self):
        """
        HandleData中传入map数据,格式如下:
          {
              折线1名称:{x:[],y:[]}
              折线2名称:{x:[],y:[]}
              ...
          }
        """
        Chart.__init__(self)
        self.grid = False
        self.title = ''
        
    def SetParam(self, **kwargs):
        """
        x_axis: x轴, 必须设置
        y_axis: y轴，必须设置
        show: 是否显示生成的图片
        chinse: 数据中是否包含中文
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
        self.title = kwargs.get('title', 'LineChart')

    def Generate(self):
        picture, chart = matplotlib.pyplot.subplots()
        for key in self.data.keys():
            value = self.data[key]
            chart.plot(value['x'], value['y'], label=key)
        chart.set(xlabel=self.x, ylabel=self.y, title = self.title)
        chart.legend()
        if self.grid:
            chart.grid()
        if self.show:
            matplotlib.pyplot.show()
        if self.save:
            picture.saveing(self.output)
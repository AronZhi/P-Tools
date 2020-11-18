import numpy
from .Chart import *

class BarChart(RectangularCoordinateChart):
    def __init__(self):
        """
        HandleData中传入map数据,格式如下:
          {
              x:[]
              名称1:[]
              名称2:[]
              ...
          }
        """
        RectangularCoordinateChart.__init__(self)
        self.barWidth = 0.3
        self.showBarValue = False
    
    def __DisplayBarValue(self, chart, rects):
        if not self.showBarValue:
            return
        for rect in rects:
            height = rect.get_height()
            chart.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    def SetParam(self, **kwargs):
        """
        barWidth: 柱的宽度
        showBarValue: 是否显示柱的y轴值
        """
        RectangularCoordinateChart.SetParam(self, **kwargs)
        self.barWidth = kwargs.get('barWidth', 0.3)
        self.showBarValue = kwargs.get('showBarValue', False)
    
    def Generate(self):
        picture, chart = matplotlib.pyplot.subplots()
        count = len(self.data) - 1
        index = 0
        if count > 1:
            index = 0 - int(count/2)
        x = numpy.arange(len(self.data['x']))
        for key in self.data.keys():
            if key == 'x':
                continue
            rects = chart.bar(x+self.barWidth/count*index, self.data[key], self.barWidth, label=key)
            self.__DisplayBarValue(chart, rects)
            index += 1
        chart.set(xlabel=self.x, ylabel=self.y, title = self.title)
        chart.legend()
        chart.grid(self.grid)
        if self.show:
            matplotlib.pyplot.show()
        if self.save:
            picture.saveing(self.output)
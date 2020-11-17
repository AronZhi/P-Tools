from .Chart import *

class LineChart(RectangularCoordinateChart):
    def __init__(self):
        """
        HandleData中传入map数据,格式如下:
          {
              折线1名称:{x:[],y:[]}
              折线2名称:{x:[],y:[]}
              ...
          }
        """
        RectangularCoordinateChart.__init__(self)

    def Generate(self):
        picture, chart = matplotlib.pyplot.subplots()
        for key in self.data.keys():
            # 画各个线条
            value = self.data[key]
            chart.plot(value['x'], value['y'], label=key)
        chart.set(xlabel=self.x, ylabel=self.y, title = self.title)
        chart.legend()
        chart.grid(self.grid)
        if self.show:
            matplotlib.pyplot.show()
        if self.save:
            picture.saveing(self.output)

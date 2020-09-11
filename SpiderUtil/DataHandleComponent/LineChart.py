from DataHandleComponent.Chart import *

class LineChart(Chart):
    def __init__(self):
        Chart.__init__(self)


    def Generate(self, x_axis, y_axis, **args):
        isGrid = args.get('grid', False)
        isShow = args.get('show', False)
        
        self.dataFrame.plot(x = x_axis, y = y_axis, kind = 'line', grid = isGrid)
        if isShow:
            matplotlib.pyplot.show()
        

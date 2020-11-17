import json
import time
from DataHandleComponent.WordCloud import *
from DataHandleComponent.LineChart import *
from DataHandleComponent.BarChart import *

def test_wordCloud():
    wordCloud = WordCloud()
    with open(os.path.join(os.path.dirname(__file__), 'Resource/minister.txt'), 'r', encoding='utf8') as fp:
        wordCloud.HandleData(fp.read())
        wordCloud.SetParam(chinse = True, fontPath = 'C:\\Windows\\Fonts\\simsun.ttc',
            backgroundFile = os.path.join(os.path.dirname(__file__), 'Resource/test1.jpg'))
        wordCloud.Generate()

def GetTestData():
    data = dict()
    with open(os.path.join(os.path.dirname(__file__), 'Resource/Performance.json'), 'r', encoding='utf8') as fp:
        jsonData = json.loads(fp.read())
        performanceData = jsonData['data']
        data['cpu_usage'] = dict()
        data['cpu_usage']['x'] = list()
        data['cpu_usage']['y'] = list()
        data['mem_usage'] = dict()
        data['mem_usage']['x'] = list()
        data['mem_usage']['y'] = list()
        startTime = 1604569450642
        for e in performanceData:
            tm = (e['time_stamp'] - startTime)/6000
            data['cpu_usage']['x'].append(tm)
            data['cpu_usage']['y'].append(e['cpu_per_all'])
            data['mem_usage']['x'].append(tm)
            data['mem_usage']['y'].append(e['mem_usage']/(1024*1024))
    return data

def test_line():
    line = LineChart()
    line.HandleData(GetTestData())
    line.SetParam(x_axis = 'Time(min)', y_axis = 'value')
    line.Generate()

def test_bar():
    bar = BarChart()
    bar.HandleData(GetTestData())
    bar.SetParam(x_axis = 'Time(min)', y_axis = 'value')
    bar.Generate()

if __name__ == '__main__':
    test_bar()
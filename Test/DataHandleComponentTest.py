from DataHandleComponent.WordCloud import *
from DataHandleComponent.LineChart import *
import sqlite3

def test_wordCloud():
    wordCloud = WordCloud()
    with open(os.path.join(os.path.dirname(__file__), 'Resource/minister.txt'), 'r', encoding='utf8') as fp:
        wordCloud.HandleData(fp.read())
        wordCloud.SetParam(chinse = True, fontPath = 'C:\\Windows\\Fonts\\simsun.ttc',
            backgroundFile = os.path.join(os.path.dirname(__file__), 'Resource/test1.jpg'))
        wordCloud.Generate()

def test_line():
    try:
        conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'Resource/rent.db'))
        sqlData = conn.execute('SELECT community, rent, area FROM RENT WHERE downtown = \'余杭\' LIMIT 20')
        data = dict()
        for row in sqlData:
            if not row[0] in data:
                e = dict()
                e['x'] = list()
                e['y'] = list()
                data[row[0]] = e
            data[row[0]]['x'].append(row[1])
            data[row[0]]['y'].append(row[2])
        lineChart = LineChart()
        lineChart.HandleData(data)
        lineChart.SetParam(x_axis = 'rent', y_axis = 'area', chinse = True)
        lineChart.Generate()
    finally:
        conn.close()

if __name__ == '__main__':
    test_line()
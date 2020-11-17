from DataHandleComponent.WordCloud import *
from DataHandleComponent.LineChart import *
import sqlite3

def test_wordCloud():
    wordCloud = WordCloud()
    with open(os.path.join(os.path.dirname(__file__), 'Resource/minister.txt'), 'r', encoding='utf8') as fp:
        wordCloud.SetData(fp.read())
        wordCloud.HandleData(chinse = True, fontPath = 'C:\\Windows\\Fonts\\simsun.ttc',
            backgroundFile = os.path.join(os.path.dirname(__file__), 'Resource/test1.jpg'))
        wordCloud.Generate()

def GetData():
    try:
        conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'Resource/rent.db'))
        sqlData = conn.execute('SELECT community, rent, area FROM RENT WHERE downtown = \'余杭\'')
        data = dict()
        for row in sqlData:
            if row[0] in data:
                data[row[0]]['rent'] += row[1]
                data[row[0]]['area'] += row[2]
            else:
                e = dict()
                e['community'] = row[0]
                e['rent'] = row[1]
                e['area'] = row[2]
                data[row[0]] = e
        lst = list()
        for k in data.keys():
            lst.append(data[k])
        return lst
    finally:
        conn.close()

def test_line():
    data = GetData()
    lineChart = LineChart()
    lineChart.SetData(data)
    lineChart.HandleData(x_axis = 'community', y_axis = 'area', chinse = True)
    lineChart.Generate()

if __name__ == '__main__':
    test_line()
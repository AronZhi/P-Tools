from DataHandleComponent.WordCloud import *
from DataHandleComponent.LineChart import *


def test_1():
    wcAssistant = WordCloud()

    with open(os.getcwd() + '\\Resource\\minister.txt', 'r', encoding='utf8') as fp:
        text = fp.read()
        wcAssistant.Generate(text = text, backgroundFile = os.getcwd() + '\\Resource\\test1.jpg', isChines = True)


def test_2():
    lineChart = LineChart()
    lineChart.SetCsvData(os.getcwd() + '\\data.csv', colum = ['downtown', 'street', 'community', 'rent', 'area'])
    lineChart.SetChineseFont()
    lineChart.Generate(x_axis = 'downtown',  y_axis = 'rent', show = True)


def test_3():
    lineChart = LineChart()
    sql = 'SELECT * FROM RENT WHERE downtown in (\'西湖\', \'余杭\')'
    lineChart.SetSqliteData('rent.db', sql)
    lineChart.SetChineseFont()
    lineChart.Generate(x_axis = 'downtown',  y_axis = 'rent', show = True)


if __name__ == '__main__':
    #test_1()
    #test_2()
    test_3()
        
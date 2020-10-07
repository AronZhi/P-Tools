from DataHandleComponent.WordCloud import *
from DataHandleComponent.Chart import *
from DbComponent.Sqlite3Mgr import *

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
    g_sqlite_mgr.GenerateDB('rent.db')
    conn = g_sqlite_mgr.GetDBConnection('rent.db')
    chart = Chart()
    downtowns = ['西湖', '余杭', '萧山', '江干', '滨江']
    frame = pandas.DataFrame()
    for downtown in downtowns:
        sql = 'SELECT downtown, SUM(rent)/SUM(area) as aveRent FROM RENT WHERE downtown = \'%s\'' % downtown
        frame = pandas.concat([frame, pandas.read_sql_query(sql, conn)])
    chart.SetData(frame)
    chart.SetChineseFont()
    chart.GeneratePie(show = True, title = 'test')


if __name__ == '__main__':
    #test_1()
    #test_2()
    test_3()
        
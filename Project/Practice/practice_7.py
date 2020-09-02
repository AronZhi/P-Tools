import numpy
import pandas
import matplotlib
from pylab import mpl

def CnShwoProblemFix():
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def test_1():
    obj = pandas.Series([-1, 0, 1, 2])
    print(obj)
    print(obj[1])

    obj2 = pandas.Series([-1, 0, 1, 2], index = ['a', 'b', 'c', 'd'])
    print(obj2)
    print(obj2['c'])

    obj3 = pandas.Series({'e': -1, 'f': 0, 'g': 1, 'h': 2})
    print(obj3)
    print(obj3 > 0)
    print(obj3[obj3 > 0])
    print(obj3 + 2)
    print(obj3 + obj2)
    print(obj3.isnull())

def test_2():
    data = {'item': ['one', 'two', 'three', 'four'],
        'year': [2000, 2001, 2002, 2003], 
        'price': [1, 2, 3, 4]}
    frame = pandas.DataFrame(data)
    print(frame)

    frame2 = pandas.DataFrame(data, columns = ['year', 'item', 'price'])
    print(frame2)

    print(frame2.T)

def test_3():
    df = pandas.read_csv('C:\\WorkSpace\\Test\\Spider\\data.csv', names = ['downtown', 'street', 'community', 'rent', 'area'])
    print(df)

    df2 = pandas.read_csv('C:\\WorkSpace\\Test\\Spider\\data.csv', nrows=5)
    print(df2)

def test_4():
    CnShwoProblemFix()
    df = pandas.read_csv('C:\\WorkSpace\\Test\\Spider\\data.csv', nrows=20, names = ['downtown', 'street', 'community', 'rent', 'area'])
    #df.plot(x='downtown', y='rent')
    #df.plot(x='downtown', y='rent', kind='bar')
    df.plot(x='downtown', y='rent', kind='pie')
    #df.plot(x='downtown', y='rent', kind='line', grid=True)
    #df.plot(x='downtown', y=['rent', 'area'], kind='bar', grid=True)
    matplotlib.pyplot.show()
    

if __name__ == '__main__':
    test_4()
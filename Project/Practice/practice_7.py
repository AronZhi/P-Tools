import pandas

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
    df = pandas.read_csv('C:\\WorkSpace\\Test\\Spider\\data.csv')
    print(df)

    df2 = pandas.read_csv('C:\\WorkSpace\\Test\\Spider\\data.csv', nrows=5)
    
    print(df2)

if __name__ == '__main__':
    test_3()
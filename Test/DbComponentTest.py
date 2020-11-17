from DbComponent.DBManager import *

manager = DBManager()

def test_1():
    manager.AddMySql('test_db', 'admin', 'P@ssword123', '10.224.84.59')
    db = manager.GetMysql('test_db')
    res = db.Query('select * from test_db.user')
    print(res)

def test_2():
    dbFile = os.path.join(os.path.dirname(__file__), 'Resource/rent.db')
    print(dbFile)
    manager.AddSqlite3(dbFile)
    conn = manager.GetSqlite3(dbFile)
    data = conn.Query('SELECT downtown, SUM(rent)/SUM(area) as aveRent FROM RENT WHERE downtown = \'西湖\'')
    #conn.Execute('CREATE TABLE RENT (downtown TEXT, street TEXT, community TEXT,rent INTEGER,area INTEGER);')
    #conn.Execute('INSERT INTO RENT (downtown, street, community, rent, area) VALUES(\'江干\', \'城东新城\', \'花园府\', 1550, 16)')
    #conn.Execute('INSERT INTO RENT (downtown, street, community, rent, area) VALUES(\'江干\', \'城东新城\', \'花园府\', 2000, 20)')
    #conn.Execute('INSERT INTO RENT (downtown, street, community, rent, area) VALUES(\'余杭\', \'闲林\', \'竹海水韵\', 1200, 20)')
    for row in data:
        print(row)

if __name__ == '__main__':
    test_2()

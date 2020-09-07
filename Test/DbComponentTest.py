from DbComponent.MySqlMgr import *
from DbComponent.Sqlite3Mgr import *
from LogComponent.LogMember import g_main_log

def test_1():
    g_mysql_mgr.GenerateDB('test_db', 'admin', 'P@ssword123', '10.224.84.59')
    db = g_mysql_mgr.GetDB('test_db')
    res = db.Query('select * from test_db.user')
    g_main_log.info(res)


def test_2():
    g_sqlite_mgr.GenerateDB('rent.db')
    db = g_sqlite_mgr.GetDB('rent.db')
    #db.Execute('CREATE TABLE RENT (downtown TEXT, street TEXT, community TEXT,rent INTEGER,area INTEGER);')
    #db.Execute('INSERT INTO RENT (downtown, street, community, rent, area) VALUES(\'江干\', \'城东新城\', \'花园府\', 1550, 16)')
    #db.Execute('INSERT INTO RENT (downtown, street, community, rent, area) VALUES(\'江干\', \'城东新城\', \'花园府\', 2000, 20)')
    #db.Execute('INSERT INTO RENT (downtown, street, community, rent, area) VALUES(\'余杭\', \'闲林\', \'竹海水韵\', 1200, 20)')
    #db.Commit()
    data = db.Query('SELECT * FROM RENT')
    for row in data:
        print(row)


if __name__ == '__main__':
    test_2()

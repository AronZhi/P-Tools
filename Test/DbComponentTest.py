from DbComponent.MySqlMgr import *
from LogComponent.LogMember import g_main_log

def main():
    g_mysql_mgr.SetDBConnectInfo('test_db', 'admin', 'P@ssword123', '10.224.84.59')
    if g_mysql_mgr.Connect('test_db'):
        db = g_mysql_mgr.GetDB('test_db')
        res = db.Query('select * from test_db.user')
        g_main_log.info(res)


if __name__ == '__main__':
    main()

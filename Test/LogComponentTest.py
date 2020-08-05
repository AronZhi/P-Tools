from LogComponent.LogMember import *

def test_1():
    g_main_log.debug('debug test')
    g_main_log.info('info test')
    g_main_log.warning('warn test')
    g_main_log.error('error test')

if __name__ == '__main__':
    test_1()
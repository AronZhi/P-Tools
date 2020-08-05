from MsgComponent.Msg import Msg
from MsgComponent.MsgType import msg_type
from LogComponent.LogMember import g_main_log

def test_1():
    msg = Msg()
    msg.data = 'hello test'
    msg.type = msg_type.unknow
    g_main_log.info(msg)

    json_text = str(msg)
    msg2 = Msg()
    msg2.parse(json_text)
    g_main_log.info(msg2)


if __name__ == '__main__':
    test_1()
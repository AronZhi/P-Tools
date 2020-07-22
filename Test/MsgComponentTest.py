from MsgComponent.Msg import Msg
from MsgComponent.MsgType import msg_type

def test_1():
    msg = Msg()
    msg.data = 'hello test'
    msg.type = msg_type.unknow
    print(msg)

    json_text = str(msg)
    msg2 = Msg()
    msg2.parse(json_text)
    print(msg2)


if __name__ == '__main__':
    test_1()
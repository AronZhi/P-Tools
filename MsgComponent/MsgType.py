class MsgType(object):
    def __init__(self):
        # 其他
        self.unknow = -1
        self.stop = 0
        # 发生异常
        self.error = 100
        self.systemError = 101
        # 正常执行结果
        self.success = 1000
        self.fail = 1001
        
msg_type = MsgType()
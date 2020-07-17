from MsgType import msg_type
import json
import time

class Msg(object):
    def __init__(self):
        self.type = msg_type.unknow
        self.data = ''

    def __repr__(self):
        tmp = {}
        tmp['type'] = self.type
        tmp['data'] = self.data
        return json.dumps(tmp)
        

    def __str__(self):
        tmp = {}
        tmp['type'] = self.type
        tmp['data'] = self.data
        return json.dumps(tmp)


    def parse(self, jsonData:str):
        obj = json.loads(jsonData)
        if type(obj) == dict:
            self.type = obj.get('type', -1)
            self.data = obj.get('data', '')


class NetPack(object):
    def __init__(self):
        self.pack = {}


    def encode(self, jsonData, host, port):
        self.pack['size'] = 0
        self.pack['header'] = '%s.%d.%d' % (host, port, time.time())
        self.pack['data'] = jsonData
        self.pack['tail'] = self.pack['header']

        text_1 = json.dumps(self.pack)
        len_1 = len(text_1)
        len_2 = len(str(len_1))
        self.pack['size'] = len_1 + len_2 - 1
        return json.dumps(self.pack)


    def __str__(self):
        return json.dumps(self.pack)


    def __repr__(self):
        return json.dumps(self.pack)


    def parse(self, jsonData:str):
        obj = json.loads(jsonData)
        if type(obj) == dict:
            self.pack['size'] = obj.get('size', 0) 
            self.pack['header'] = obj.get('header', '')
            self.pack['data'] = obj.get('data', '')
            self.pack['tail'] = obj.get('tail', '')

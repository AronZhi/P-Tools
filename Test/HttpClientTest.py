from NetComponent.Http.Client import *

def stop():
    client = Client()
    client.Get('http://10.224.84.217:8888/?command=stop')

def get():
    command = input('Please command: ')
    client = Client()
    client.Get('http://10.224.84.217:8888/?command=%s' % command)

def post():
    data = input('Please input data: ')
    client = Client()
    dataDict = dict()
    dataDict['echo'] = data
    client.Post('http://10.224.84.217:8888/', dataDict)

def headers():
    client = Client()
    client.updateSession(headers = {"Content-Type": "application/json"})
    msg = '{"client_version" : "40.12.0.159", "conf_id" : "176421468506168610", "cpu" : {"core" : 8, "freq" : "2.112000"}}'
    content = '{"echo": ' + msg + '}'
    client.Post('http://10.224.84.217:8888/', content.encode())

if __name__ == '__main__':
    stop()
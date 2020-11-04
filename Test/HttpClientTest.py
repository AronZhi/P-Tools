import requests
import urllib

def __handleRes(response):
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.status_code)

def stop():
    r = requests.get('http://127.0.0.1:8888/?command=stop')
    __handleRes(r)

def post():
    dataDict = dict()
    msg = '{"client_version" : "40.12.0.159", "conf_id" : "176421468506168610", "cpu" : {"core" : 8, "freq" : "2.112000"}}'
    dataDict['echo'] = msg
    r = requests.post('http://127.0.0.1:8888/', data=dataDict)
    __handleRes(r)

def post2():
    msg = '{"client_version" : "40.12.0.159", "conf_id" : "176421468506168610", "cpu" : {"core" : 8, "freq" : "2.112000"}}'
    content = '{"echo": ' + msg + '}'
    r = requests.post('http://127.0.0.1:8888/', data=content.encode(), headers={"Content-Type": "application/json"})
    __handleRes(r)

if __name__ == '__main__':
    stop()
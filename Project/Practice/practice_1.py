import requests

def test_1():
    """
    通过requests库请求网页数据
    """
    try:
        response = requests.get('http://top.baidu.com/buzz?b=341&c=513&fr=topcategory_c513')
        if response.status_code == 200:
            print(response.text)
        else:
            print('response:%d' % response.status_code)
    except requests.exceptions as requestErr:
        print('request err', requestErr)
    except Exception as e:
        print("except:",e)
    return


def test_2():
    """
    增加request header来规避反爬
    """
    try:
        header = {'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        response = requests.get('http://top.baidu.com/buzz?b=341&c=513&fr=topcategory_c513', headers = header)
        if response.status_code == 200:
            print(response.text)
        else:
            print('response:%d' % response.status_code)

    except requests.exceptions as requestErr:
        print('request err:', requestErr)
    except Exception as e:
        print("except:",e)
    return

def test_3():
    """
    修改编码来显示中文
    """
    try:
        header = {'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        response = requests.get('http://top.baidu.com/buzz?b=341&c=513&fr=topcategory_c513', headers = header)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            print(response.text)
        else:
            print('response:%d' % response.status_code)

    except requests.exceptions as requestErr:
        print('request err:', requestErr)
    except Exception as e:
        print("except:",e)
    return

def main():
    #test_1()
    #test_2()
    test_3()


if __name__ == '__main__':
    main()
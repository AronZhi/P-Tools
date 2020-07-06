import requests

def test_1():
    try:
        response = requests.get('https://book.douban.com/')
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
    try:
        header = {'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        response = requests.get('https://book.douban.com/', headers = header)
        if response.status_code == 200:
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
    test_2()


if __name__ == '__main__':
    main()
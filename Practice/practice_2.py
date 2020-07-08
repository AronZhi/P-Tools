import requests
import re
import bs4

def GetHtml():
    try:
        header = {'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        response = requests.get('http://top.baidu.com/buzz?b=341&c=513&fr=topcategory_c513', headers = header)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response.text
        else:
            return 'response:%d' % response.status_code

    except requests.exceptions as requestErr:
        return 'request err:' + requestErr
    except Exception as e:
        return 'except:' + e

def test_1():
    """
    用正则来解析
    """
    html = GetHtml()
    lst = re.findall('w=(?:%[A-Z0-9][A-Z0-9]){2,}">.*</a', html) #python的()中需加入?:来防止进入捕获模式
    res = []
    for item in lst:
        start = item.find('>')
        end = item.find('<')
        res.append(item[start + 1 : end])
    print(res)
    return

def test_2():
    """
    用beautiful soup来解析
    """
    html = GetHtml()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    lst = soup.find(class_ = 'list-table').find_all(class_ = 'list-title')
    for item in lst:
        print(item.text)

def main():
    test_1()
    #test_2()
    return

if __name__ == '__main__':
    main()
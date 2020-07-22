from SpiderComponent.Spider import *


def main():
    spider = Spider()
    spider.Crawl('https://www.runoob.com/python3/python3-file-methods.html')
    return


if __name__ == '__main__':
    main()
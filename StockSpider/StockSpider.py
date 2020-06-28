from StockListSpider import *
from StockHolderSpider import *

def main()->int:
    """
    stockLst = StockListSpider()
    stockLst.Crawl()
    """
    stockHolders = StockHolderSpider()
    stockHolders.Crawl()
    return 0


if __name__ == '__main__':
    main()

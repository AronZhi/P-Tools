## Build
* 需要将Spider加入到python搜索路径
```
运行AddSource.py, 输入指定的路径
```

## DbComponent
* 数据库操作类，操作MySQL

## MsgComponent
* 消息传输和定义

## SpiderComponent:
* 爬虫基类， 需要自定义HandleMsg完成网页处理

## WordCloud
* 词云类，生成词云

## Test
* 测试代码

## Project
### Practice
* 爬虫学习代码

### RentSpider
* 房租爬虫，爬取链家网杭州地区最新上架的租房信息，爬取数据保存在csv文件中。
* 爬取的字段：城区，街道，小区，房租，面积。

### StockSpider
* 股票爬虫，爬取东方财富股票信息。
* 爬取的字段：十大流通股东
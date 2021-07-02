## 环境
* python3.7以上
* 需要将Spider加入到python搜索路径
    ```
    运行AddSource.py, 输入utilcomponent所在路径
    ```

## Common
* 一些常用的工具，比如单例装饰器，函数log装饰器，logger
  
## DbComponent
* 需要PyMySQL 0.9.3
* 数据库操作类，操作MySQL, InfluxDB

## NetComponet
* 需要tornado 6.0.4
* 网络操作相关, http提供了支持异步io的http server和http client
  
## CMakeAssistant
* 将固定格式的json文件转换成CMakeList文件

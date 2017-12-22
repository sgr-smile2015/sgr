
### 使用说明

脚本可以使用python监控目录的日志关键字
变化情况,并汇成rrd图表在ganglia-web上
展示

1.默认读取的配置文件为config,返回一个
{'dao': '/mnt/log/dao.log',
'user': '/data/user/user.log'
}

2.读取日志关键字默认为ERROR,这个可以修改

3.现在有个bug,如果日志文件每天都用logrotate
做相应的切分轮转,该脚本也必须做相应的自启动

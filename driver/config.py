#!/usr/bin/env python

def url():
    url = "http://139.196.43.67:8080/"
    return url

# mock 开关
def mock_open():
    open = 'ON'
    return open

#数据库连接串

sql_conn_dic ={
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':"123",
    'db':'test',
    'charset':'utf8'
}


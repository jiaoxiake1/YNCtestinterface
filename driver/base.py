#!/usr/bin/env python

from driver import config,HttpServer,read_execl,write_execl
import json
import requests



def get_url(EndPoint):
    host = config.url()
    endpoint = EndPoint
    url = "".join([host,endpoint])
    return url


def get_response(url,Methon,**DataALL):
    global resp
    if Methon == "post":
        resp = HttpServer.MyHTTP().post(url,**DataALL)
    elif Methon == "get":
        resp = HttpServer.MyHTTP().get(url,**DataALL)

    return resp

#获取整个sheet 信息
def get_data(testfile,sheetname):
    datainfo = read_execl.XLDatainfo(testfile)
    Data = datainfo.get_sheetinfo_by_name(sheetname)
    return Data

# insert data

def insert_data_one_line(testfile,insert_text,sheetname,row):
    datainfo = write_execl.XLDataInsert(testfile,insert_text)
    datainfo.insertData_by_sheetname(sheetname,row)

# insert several lines data

def insert_data_several_lines(testfile,insert_text,sheetname):
    datainfo = write_execl.XLDataInsert(testfile,insert_text)
    datainfo.insertData_by_sheetname_lines(sheetname)



# 获取token

def login_token():

    url = "http://139.196.43.67:8080/login"
    payload = {"username":"nn.chen@yuneec.com","password":"a1234567890"}
    payload = json.dumps(payload)
    r = requests.post(url,data=payload)
    result = r.json()
    # print(result["data"])
    # print((result["data"])["token"])
    return ((result["data"])["token"])





# #获取sheet 某一列信息
# def get_data_by_columns(testfile,sheetname,column):
#     datainfo = read_execl.XLDatainfo(testfile)
#     Data = datainfo.get_sheetinfo_by_name_columns(sheetname,column)
#     return Data
#
# #获取sheet 某一列信息，并转换为二维数组
#
# def get_data_by_columns_array(testfile,sheetname,column):
#     datainfo = read_execl.XLDatainfo(testfile)
#     Data = datainfo.get_sheetinfo_by_name_by_column(sheetname,column)
#     return Data

# def get_mock_status():
#     mock_status = config.mock_open()
#     return mock_status

#将数据装进数组

# def insertArray(strs):
#     insertArr = []
#     for i in range(0,3):
#         insertArr.append(strs)
#     return insertArr



if __name__ =="__main__":
    login_token()
#!/usr/bin/env python

from driver import config,HttpServer,read_execl



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

#获取整个sheeet 信息
def get_data(testfile,sheetname):
    datainfo = read_execl.XLDatainfo(testfile)
    Data = datainfo.get_sheetinfo_by_name(sheetname)
    return Data

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

def get_mock_status():
    mock_status = config.mock_open()
    return mock_status


if __name__ =="__main__":
    print()
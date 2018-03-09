#!/usr/bin/env python
import pymysql
import os
from driver import config

from pymysql.err import OperationalError

class DB(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(**config.sql_conn_dic)
            # self.cur = self.conn.cursor()

        except OperationalError as e:
            print("MySql Error %s"% e)
        except Exception as e1:
            print("myError %s"% e1)
    #删除表数据
    def clear(self,table_name):
        real_sql = "delete from "+table_name+";"
        with self.conn.cursor() as cur:
            cur.execute("SET FOREIGN_KEY_CHECKS=0;")
            cur.execute(real_sql)
        self.conn.commit()

    # 插入表数据
    def insert(self,table_name,table_data):
        for key,value in table_data:
            # print("key : "+str(key))
            # print("value : " + str(value))
            table_data[key] = "'"+str(table_data[key])+"'"
            key = ",".join(table_data.keys())
            value = ",".join(table_data.values())
            real_sql = "INSERT INTO "+table_name+"( "+key+" ) VALUES ("+value+")"
            print(real_sql)

            with self.conn.cursor() as cur:
                cur.execute(real_sql)
            self.conn.commit()

    #关闭数据库连接

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = DB()
    table_name = "test1"
    data = {"id":11,"name":"10"}
    db.clear(table_name)
    db.insert(table_name,data)
    db.close()







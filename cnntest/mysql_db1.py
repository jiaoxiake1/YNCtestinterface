#!/usr/bin/env python
import pymysql
from driver import config

'''数据库'''


'''1、建立连接，创建游标'''
conn = pymysql.connect(**config.sql_conn_dic)
# print(config.sql_conn_dic)
cur = conn.cursor()


"""2、数据库操作"""
# name = "A"
# code = (("A","1"),)
# sql = "select * from test1 WHERE  name=%s and sex = %s"

# cur.execute(sql)
# cur.execute(sql,name) 只支持一个参数
# print(cur.fetchmany(2))
# print(cur.fetchone())
# cur.executemany(sql,code)
# print(cur.fetchall())

# print(cur.rowcount)

"""增删改"""

# sql1 = "update test1 set name='EE' where name = 'ee'"
# sql2 = "update test1 set name='EEEEEEEEEEEEEEEEE' where name = 'f'"
# # try:
#     cur.execute(sql1)
#     cur.execute(sql2)
#     conn.commit() #提交事务
#     print('Ture')
# except Exception as e:
#     conn.rollback()
#     print(e,'Fasle')

# print(cur.fetchone())

# print(cur.rowcount)
sql = "select * from test1"
sql = " delete from test1 where id='1'"
cur.execute(sql)
conn.commit()
print(cur.fetchall())


"""3、关闭游标，关闭数据库连接"""
cur.close()
conn.close()
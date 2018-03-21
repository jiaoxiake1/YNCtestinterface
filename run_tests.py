#!/usr/bin/env python
import time,sys,os
sys.path.append('./interface')
import HTMLTestRunner1
import unittest
import smtplib
from email.mime.text import MIMEText  #定义邮件正文
from email.mime.multipart import MIMEMultipart # 邮件附件
from email.header import Header #邮件标题



# 定义发送邮件

def send_mail(file_new):


    smtpserver = "smtp.qq.com"
    user = "760877038@qq.com"
    password = "kpnkijksgjxfbdjf"

    sender = "760877038@qq.com"
    receivers = ["1065853762@qq.com", "760877038@qq.com"]
    subject = "YNC webserver interface 自动化测试报告"


    f = open(file_new,"rb")
    mail_body = f.read()
    f.close()

    #构造附件内容
    send_file = open(filename, 'rb').read()
    att = MIMEText(send_file, "base64", "utf-8")
    att['Content-Type'] = "application/octet-stream"
    att['Content-Disposition'] = 'attachent;filename='+file_path



    # 构建发送接收信息
    msgRoot = MIMEMultipart()
    msgRoot.attach(MIMEText(mail_body,"html","utf-8"))
    msgRoot["Subject"] = subject
    msgRoot["From"] = sender
    msgRoot["To"] = ','.join(receivers)
    print(msgRoot["To"])
    msgRoot.attach(att)


    smtp = smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo()
    smtp.ehlo()
    smtp.login(user,password)

    print("start send email....")
    smtp.sendmail(sender,receivers,msgRoot.as_string())
    smtp.quit()
    print("send email end!")

# 查找测试报告的目录，找到最新的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    print(lists)
    lists.sort(key = lambda fn:os.path.getmtime(testreport+"\\"+fn))# fn 是临时定义的变量，一次从lists 中取值赋值给 fn ;
                                                                    # os.path.getmtime(testreport+"\\"+fn) 获取每个文件的时间
                                                                    # lists.sort 按照时间从小到大给lists 排序

    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new



#指定测试用例是当前文件加下的interface 目录

test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__ == "__main__":
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/'+now+'result.html'

    fb = open(filename,"wb")
    runner = HTMLTestRunner1.HTMLTestRunner(stream=fb, title='Yuneec UC server interface test',
                                            description='yuneec server interface test')

    runner.run(discover)
    fb.close()
    file_path =new_report("./report/")
    print(filename)
    send_mail(file_path)

# -*- coding: UTF-8 -*-
import requests
from lxml import etree
from prettytable import PrettyTable
import smtplib

from email.mime.text import MIMEText
import os
import time
def getinfor(x ,i,html):
     strxpath = '//table[@align="left"]/tr['+str(i)+']/td';
     html_data = html.xpath(strxpath);

     x.add_row([html_data[0].text, html_data[1].text, html_data[2].text, html_data[3].text, html_data[4].text,
                html_data[5].text, html_data[6].text, html_data[7].text]);
     return x






request = requests.get("http://www.boc.cn/sourcedb/whpj/")

request.encoding="utf-8";
htmlresult = request.text.encode("utf-8")
# print htmlresult
html = etree.HTML(htmlresult)
title_data = html.xpath('//table/tr/th')
titlestr = ""

x = PrettyTable([title_data[0].text,title_data[1].text,title_data[2].text,title_data[3].text,title_data[4].text,title_data[5].text,title_data[6].text,title_data[7].text]);
x.padding_width = 1
x.align[title_data[0].text] = "1"

for k in range(2,29,1):
    x =  getinfor(x,k,html);


# _user = "13430365600@163.com"
# _pwd = "sam960522"
# _to = ["379521061@qq.com","summerliu@live.com"];
# x.encoding="utf8"
# con = x.__str__()+"\n";
# con = con + "政政实时汇率监控脚本使用中";
# # 使用MIMEText构造符合smtp协议的header及body
# msg = MIMEText(con,_charset="utf-8")
# msg["Subject"] = u"当前exchange rate"
# msg["From"] = _user
# msg["To"] = ",".join(_to)
#
# s = smtplib.SMTP("smtp.163.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
# s.login(_user, _pwd)  # 登陆服务器
# s.sendmail(_user, _to, msg.as_string())  # 发送邮件
# print "send succeed"
# s.close()
print x



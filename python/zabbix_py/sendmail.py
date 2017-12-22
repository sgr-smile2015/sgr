#!/usr/bin/python
# -*- coding:utf-8 -*-
  
import smtplib
import sys
from email.mime.text import    MIMEText
from email.header import Header
import time
#reload(sys)
#sys.setdefaultencoding('utf8')
current_time=time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
  
mail_host ='smtp.exmail.qq.com'
mail_user ='yangxx00@163.com'
mail_pwd = 'xxo02016'
  
def send_email( content,mailto, get_sub ):
    #msg = MIMEText( content.encode('utf8'),_subtype = 'html', _charset = 'utf8')
    #msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['From'] =mail_user
    msg['Subject'] =get_sub
    msg['To'] = ",".join( mailto )
    
    try:
        s = smtplib.SMTP_SSL( mail_host, 465)       
        s.login(mail_user, mail_pwd )
        s.sendmail(mail_user, mailto,msg.as_string())
        s.close()
    except Exception as e:
        print 'Exception: ', e
  
title=sys.argv[2]
cont="""
---------------------------------
摘要:  %s
---------------------------------
时间: %s
---------------------------------
  
"""%(sys.argv[3],current_time)
  
  
to_list = [
         '%s'%(sys.argv[1]),
        ]
  
with    open('/tmp/sendmail_qs.log','ab') as f:
        f.write('%s  Receive address:  %s Title: %s \n'%(current_time,sys.argv[1],title))
send_email(cont, to_list,title)

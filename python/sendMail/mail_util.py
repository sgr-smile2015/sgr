#!/usr/bin/python
#-*- coding:utf-8 -*-

#import sys
import os
import smtplib
import time
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.header import Header
#reload(sys)


class Mail(object):

    def __init__(self):
        self.user = "notify@163.com"
        self.password = "xxoo"
        self.__mail_list = "./maillist.test"
        self.__html_file = "./att/result.html"
        self.__excel_path = "./excel"

    def __read_file(self):
        ret = list()
        with open(self.__mail_list) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                ret.append(line)
        return ret

    def __file_text(self):
        output = ""
        with open(self.__html_file) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                output += line
        return output

    def __ret_attach(self):
        attach_file = list()
        for j in os.listdir(self.__excel_path):
            attach_file.append("{}/{}".format(self.__excel_path, j.encode("utf-8")))
            print "attach_file:{}".format(",".join(attach_file))
        return attach_file

    def send_mail(self, send_from, send_to, subject, html, files=None, server="smtp.exmail.qq.com"):
        assert isinstance(send_to, list)
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = COMMASPACE.join(send_to)
        msg['Date'] = formatdate(localtime=True)
        subject_encode = Header(subject, 'utf-8')
        msg['Subject'] = subject_encode
        msg.attach(MIMEText(html, "html", 'utf-8'))

        for f in files or []:
            file_basename = basename(f).decode('utf-8').encode('gb2312')
            with open(f, "rb") as fi:
                part = MIMEApplication(fi.read(), Name=file_basename)
                part['Content-Disposition'] = 'attachment; filename="%s"' % file_basename
                msg.attach(part)

        smtp = smtplib.SMTP(server)
        smtp.login(self.user, self.password)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()

    def send(self, subject):
        html_content = self.__file_text()
        send_list = self.__read_file()
        attach_file = self.__ret_attach()
        for k in send_list:
            print "send mail to:{}".format(k)
            self.send_mail("notify@163.com", [k, ], subject, html_content, files=attach_file)
            time.sleep(2)

#m = Mail()
#m.send('邮件测试 Mail...')

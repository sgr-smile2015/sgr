#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import os
import smtplib
reload(sys)
import time
import random
#sys.setdefaultencoding("utf-8")
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.header import Header

#user = "postmaster"
#password = "suChe$huP6ar"
user = "notify@163.com"
password = "123"


def send_mail(send_from, send_to, reply_to, subject, text, html, files=None,
              #server="smtp.service.ipin.com"):
              server="smtp.exmail.qq.com"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    subject_encode = Header(subject, 'utf-8')
    msg['Subject'] = subject_encode
    msg['Reply-To'] = reply_to

    #msg.attach(MIMEText(text, "plain", 'utf-8'))
    msg.attach(MIMEText(html, "html", 'utf-8'))

    for f in files or []:
        file_basename = basename(f).decode('utf-8').encode('gb2312')
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=file_basename
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % file_basename
            msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.login(user, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

def file2text(file_name):
    output = ""
    with open(file_name) as f:
        while True:
            line = f.readline()
            if not line: break
            output += line
    return output


def read_file(file_name):
    with open(file_name) as f:
        while True:
            line = f.readline()
            if not line: break
            line = line.strip()
            yield line


if __name__ == "__main__":
    to_list_file = sys.argv[1]
    to_list = []
    for i in read_file(to_list_file):
        to_list.append(i)
    print to_list
    reply_to = "163@163.com"
    
    subject = sys.argv[2]
    text_content = file2text("att/result.txt")
    html_content = file2text("att/result.html") 

    attach_file = []
    path = "att"
    for j in os.listdir(path):
        attach_file.append("{}/{}".format(path, j.encode("utf-8")))
    print "attach_file:{}".format(",".join(attach_file))

    for k in to_list:
        print "sendmail to:{}".format(k)
        try:
            send_mail("notify@ipin.com", [k,], reply_to, subject, text_content, html_content, files=attach_file)
            sleep_time = random.randint(5, 10)
            time.sleep(sleep_time)
        except:
            import traceback
            traceback.print_exc()

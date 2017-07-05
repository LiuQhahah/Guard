#!/usr/bin/env python3
#coding: utf-8
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage 

sender = '1192395260@qq.com'
receiver = 'liuq_1995@163.com'
subject = 'python email test'
smtpserver = 'smtp.qq.com'
username = '1192395260@qq.com'
password = 'lpwyyjeapiczgchd'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message' 

cartella = "E:\\img"
os.chdir(cartella)

filelist = os.listdir(os.getcwd())
filelist = filter(lambda x: not os.path.isdir(x),filelist)

attachment = max(filelist,key = lambda x:os.stat(x).st_mtime)
path_img = os.path.abspath(attachment)
#¹¹Ôì¸½¼þ
#att = MIMEText(open('e:\\img\\weekly.png', 'rb').read(), 'base64', 'utf-8')
att = MIMEText(open(path_img, 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename=camera.jpg'
msgRoot.attach(att) 

try:
	smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
	smtp.login(username, password)
	smtp.sendmail(sender, receiver, msgRoot.as_string())
	smtp.quit()
	print "Success!"
except smtplib.SMTPException,e:
	print "Failed,%s"%e
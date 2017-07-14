#!/usr/bin/env python3
#coding: utf-8
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage 
import logging
import time
class SendEmail:

	
	
	def main(self):
		sender = '1192395260@qq.com'
		receiver = 'lei.z@njupt.edu.cn'
		subject = 'python email test'
		smtpserver = 'smtp.qq.com'
		username = '1192395260@qq.com'
		password = 'peyomxkrntlyfjed'

		msgRoot = MIMEMultipart('related')
		msgRoot['Subject'] = ' message from Arduino' 

		cartella = '/mnt/sda2/webcam/'
		os.chdir(cartella)
		logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='/mnt/sda2/pgm/camera.log',  
                    filemode='w')
		
		
		filelist = os.listdir(os.getcwd())
		filelist = filter(lambda x: not os.path.isdir(x),filelist)

		attachment = max(filelist,key = lambda x:os.stat(x).st_mtime)
		path_img = os.path.abspath(attachment)

		att = MIMEText(open(path_img, 'rb').read(), 'base64', 'utf-8')
		att["Content-Type"] = 'application/octet-stream'
		att["Content-Disposition"] = 'attachment; filename=camera_from_ArduinoYUN.jpg'
		msgRoot.attach(att) 
		
		
		try:
			smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
			smtp.login(username, password)
			
			smtp.sendmail(sender, receiver, msgRoot.as_string())
			smtp.quit()
			logging.info('Success to 5min  lei.z@njupt.edu.cn')
			print "Success"
			
		except smtplib.SMTPException,e:
			print "Failed,%s"%e
			logging.error("error to 5min  lei.z@njupt.edu.cn")
		
		
			


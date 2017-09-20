######################################################################
#       Send_Email.py
#
# This snippet code sending email with smtp protocol
######################################################################

import smtplib
import RPi.GPIO as GPIO
import time

GmailUser = 'reza.raspberrypi@gmail.com' 
GmailPass = '123456654' 
SmtpServer = 'smtp.gmail.com' 
SmtpPort = 587

def SendEmail(recipient, subject, text):    
    smtpServer = smtplib.SMTP(SmtpServer, SmtpPort)    
    smtpServer.starttls()      
    smtpServer.login(GmailUser, GmailPass)    
    header = 'To:' + recipient + '\n' + 'From: ' + GmailUser    
    header = header + '\n' + 'Subject:' + subject + '\n'    
    msg = header + '\n' + text + ' \n\n'    
    smtpServer.sendmail(GmailUser, recipient, msg)    
    smtpServer.quit()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN, pull_up_down = GPIO.PUD_UP)
counter = 0

while(1):
    if(GPIO.input(18) == 0):
        print("Danger!!!!!!")
	print("sending email...")
        SendEmail('arjmandi.re@gmail.com', 'Danger: home security!', 'Button Pressed-number: ' + str(counter))
        print("send complete")
        counter = counter + 1
        
        

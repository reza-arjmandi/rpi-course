import smtplib
import RPi.GPIO as GPIO
import time

GMAIL_USER = 'reza.raspberrypi@gmail.com' 
GMAIL_PASS = '123456654' 
SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587

def send_email(recipient, subject, text):    
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)    
    smtpserver.starttls()      
    smtpserver.login(GMAIL_USER, GMAIL_PASS)    
    header = 'To:' + recipient + '\n' + 'From: ' + GMAIL_USER    
    header = header + '\n' + 'Subject:' + subject + '\n'    
    msg = header + '\n' + text + ' \n\n'    
    smtpserver.sendmail(GMAIL_USER, recipient, msg)    
    smtpserver.quit()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while(1):
    if(GPIO.input(18)==1):
        print("Danger: Movement Detect!")
        print("sending email...")
        send_email('arjmandi.re@gmail.com', 'Danger: home security!', 'Anonymous Movement Detected')
        print("send complete")
        time.sleep(10)
        

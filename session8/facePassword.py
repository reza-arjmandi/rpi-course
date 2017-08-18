import picamera
import time
from SimpleCV import Color, Image, np
import RPi.GPIO as GPIO

quality = 400
minMatch = 0.3

RedLED = 18
GreenLED = 23
YellowLED = 24

try:
    password = Image("password.jpg")
except:
    password = None
 
mode = "unsaved"
saved = False
minDist = 0.25

GPIO.setmode(GPIO.BCM)
GPIO.setup(RedLED, GPIO.OUT)
GPIO.setup(GreenLED, GPIO.OUT)
GPIO.setup(YellowLED, GPIO.OUT)

GPIO.output(GreenLED, 0)
GPIO.output(RedLED, 0)
GPIO.output(YellowLED, 0)

with picamera.PiCamera() as camera:
 while True:
    camera.start_preview()
    time.sleep(5)
    camera.capture('pifacepw.jpg')
    image=Image("pifacepw.jpg")
    camera.stop_preview()
    faces = image.findHaarFeatures("face.xml") 
    if faces:
        if not password:
            faces.draw()
            face = faces[-1]
            password = face.crop().save("password.jpg")
            print "First Run Application"
            print "Exit Program"
            break
        else:
            faces.draw()
            face = faces[-1]
            template = face.crop()
            template.save("passwordmatch.jpg")
            template = Image("passwordmatch.jpg")
            diff = template.resize(password.width, password.height) - password;
            print(diff)
            #keypoints = password.findKeypointMatch(template)

            if diff.findBlobs(minsize = 20000):
                print "Face not matched"
                print "Danger"
                GPIO.output(GreenLED, 0)
                GPIO.output(RedLED, 1)
                GPIO.output(YellowLED, 0)
                     
            else:
                print "your face detected and matched"
                print "Welcome to Application"
                GPIO.output(GreenLED, 1)
                GPIO.output(RedLED, 0)
                GPIO.output(YellowLED, 0)
    else:
        print "No face found"
        print "Please look at the camera"
        GPIO.output(GreenLED, 0)
        GPIO.output(RedLED, 0)
        GPIO.output(YellowLED, 1)
 

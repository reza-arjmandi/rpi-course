from picamera import PiCamera
from picamera.array import PiRGBArray
from PIL import Image
import numpy
import cv2

frameSize = (320, 240)
camera = PiCamera()
camera.resolution = frameSize
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=frameSize)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def DetectFacesAndEyes(mat):
    gray = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(mat, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roiGray = gray[y:y + h, x:x + w]
        roiColor = mat[y:y + h, x:x + w]
        eyes = eyeCascade.detectMultiScale(roiGray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roiColor, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

#main loop
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    mat = frame.array
    DetectFacesAndEyes(mat)
    cv2.imshow('frame', mat)
    rawCapture.truncate(0)
    if(cv2.waitKey(1) and 0xFF == ord('q')):
        break

cv2.destroyAllWindows()

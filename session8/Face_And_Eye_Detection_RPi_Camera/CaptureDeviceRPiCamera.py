from picamera import PiCamera
from picamera.array import PiRGBArray
from PIL import Image
import numpy
import cv2

class CaptureDeviceRPiCamera:
    def __init__(self, frameSize, frameRate):
        camera = PiCamera()
        camera.resolution = frameSize
        camera.framerate = frameRate
        rawCapture = PiRGBArray(camera, size=frameSize)
        self.bufferIter = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
        self.framCount = 0;

    def GrabFrame(self, gray):
        mat = self.bufferIter[0].array
        self.frameCount +=1
        if(not gray):
            return mat

        return cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)


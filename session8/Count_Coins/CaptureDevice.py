import cv2
class CaptureDevice:
    def __init__(self, mode, address):
        self.inputMode = mode
        self.addressFile = address
        if(mode == "-v"):
            self.cap = cv2.VideoCapture(address)
        if(mode == "-w"):
            self.cap = cv2.VideoCapture(0)

    def GrabFrame(self, gray):
        if(self.inputMode == "-i"):
            if(not gray):
                return cv2.imread(self.addressFile)
            return cv2.imread(self.addressFile, 0)

        elif(self.inputMode == "-v" or self.inputMode == "-w"):
            if(self.inputMode == "-v"):
                if(not self.cap.isOpened()):
                    return
            ret, frame = self.cap.read()
            if(not gray):
                return frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return gray
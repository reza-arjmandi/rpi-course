import cv2
import CaptureDeviceRPiCamera

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

if __name__ == "__main__":
    device = CaptureDeviceRPiCamera.CaptureDeviceRPiCamera((320, 240), 32)
    while(True):
        frame = device.GrabFrame(False)
        DetectFacesAndEyes(frame)
        cv2.imshow('frame', frame)
        if(cv2.waitKey(1) and 0xFF == ord('q')):
            break

cv2.destroyAllWindows()

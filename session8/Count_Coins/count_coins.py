import cv2
import numpy as np
import sys
import CaptureDevice

def CountCoins(img, cimg):
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

if __name__ == "__main__":
    captureDevice = CaptureDevice.CaptureDevice(sys.argv[1], sys.argv[2])
    while(True):
        img = captureDevice.GrabFrame(True)
        img = cv2.medianBlur(img, 5)
        cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        CountCoins(img, cimg)
        cv2.imshow('detected circles',cimg)
        if (cv2.waitKey(1) and 0xFF == ord('q')):
            break

    cv2.destroyAllWindows()
import picamera
import SimpleCV
import PIL
from io import BytesIO

camera = picamera.PiCamera()
camera.resolution=(640,480)
camera.framerate=24

def get_camera_image():    
    buf = BytesIO()
    camera.capture(buf, "rgb")
    im = PIL.Image.frombuffer("RGB", (640, 480), buf.getvalue(), "raw", "RGB", 0,1)
    result = SimpleCV.Image(im)
    return result
            
while True:
    i = get_camera_image().invert()
    i.show()
    coins = i.findCircle(canny=100, thresh=70, distance=150)
    try:
        print(len(coins))
        coins.draw(width=4)
        coins.show()
    except:
        print(0)

    

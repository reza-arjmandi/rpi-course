import picamera
import SimpleCV
import PIL
from io import BytesIO

camera = picamera.PiCamera()
camera.resolution=(320,240)
camera.framerate=24

def get_camera_image():    
    buf = BytesIO()
    camera.capture(buf, "rgb")
    im = PIL.Image.frombuffer("RGB", (320, 240), buf.getvalue(), "raw", "RGB", 0,1)
    result = SimpleCV.Image(im)
    return result
            
while True:
    i = get_camera_image()
    faces = i.findHaarFeatures('face.xml',min_neighbors=5)
    faces.draw(width=4)
    i.show()
    try:
        print(len(faces))
    except:
        print(0)
    

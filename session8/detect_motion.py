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

MIN_BLOG_SIZE = 70000

old_image = get_camera_image()

while True:
    new_image = get_camera_image()
    diff = new_image - old_image
    blobs = diff.findBlobs(minsize=MIN_BLOG_SIZE)
    if blobs :
        print("Movement detected")
    old_image = new_image
    print('.')

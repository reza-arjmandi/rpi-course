######################################################################
#       OLED_Clock.py
#
# This program display date and time on OLED module
######################################################################

import Adafruit_SSD1306
from datetime import datetime
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Setup Display
RST=24
device = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
device.begin()
device.clear()
device.display()
width = device.width
height = device.height

fontFile = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
smallFont = ImageFont.truetype(fontFile, 12)
largeFont = ImageFont.truetype(fontFile, 33)

# Display a message on 3 lines, first line big font        
def DisplayMessage(line1, line2):
    global device
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    draw.text((10, 0),  line1, font=smallFont, fill=255)
    draw.text((0, 20),  line2, font=largeFont, fill=255)
    device.image(image)
    device.display()

while True:
    now = datetime.now()
    dateMessage = '{:%d %B %Y}'.format(now)
    timeMessage = '{:%H:%M:%S}'.format(now)
    DisplayMessage(dateMessage,timeMessage)
    time.sleep(0.1)

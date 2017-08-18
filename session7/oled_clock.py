#!/usr/bin/env python


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

font_file = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
small_font = ImageFont.truetype('FreeSans.ttf', 12, filename=font_file)
large_font = ImageFont.truetype('FreeSans.ttf', 33, filename=font_file)

# Display a message on 3 lines, first line big font        
def display_message(top_line, line_2):
    global device
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    maxwidth, unused = draw.textsize(top_line, font=large_font)
    #with canvas(deviccd e) as draw:
    draw.text((10, 0),  top_line, font=small_font, fill=255)
    draw.text((0, 20),  line_2, font=large_font, fill=255)
    device.image(image)
    device.display()

while True:
    now = datetime.now()
    date_message = '{:%d %B %Y}'.format(now)
    time_message = '{:%H:%M:%S}'.format(now)
    display_message(date_message,time_message)
    time.sleep(0.1)

######################################################################
#       OLED_Image.py
#
# This program load an image and display on OLED module
######################################################################

import time
import Adafruit_SSD1306
from PIL import Image

# Raspberry Pi pin configuration:
RST = 24

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

image = Image.open('happycat_oled_64.ppm').convert('1')

# Display image.
disp.image(image)
disp.display()

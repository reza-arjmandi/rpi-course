######################################################################
#       OLED_Animate.py
#
# This program display a long message with sinusoid wave effect on
# OLED module
######################################################################

import math
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Raspberry Pi pin configuration:
RST = 24

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))

# Load default font.
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
text = "9th Raspberry Pi Course ********** Shahed University"
maxWidth, unused = draw.textsize(text, font=font)

# Set animation and sine wave parameters.
amplitude = height / 4
offset = height / 2 - 4
velocity = -2
startPos = width

print('Press Ctrl-C to quit.')
pos = startPos
while True:
    # Clear image buffer by drawing a black filled box.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Enumerate characters and draw them offset vertically based on a sine wave.
    x = pos
    for i, c in enumerate(text):
        # Stop drawing if off the right side of screen.
        if x > width:
            break
        # Calculate width but skip drawing if off the left side of screen.
        if x < -10:
            charWidth, charHeight = draw.textsize(c, font=font)
            x += charWidth
            continue
        # Calculate offset from sine wave.
        y = offset + math.floor(amplitude * math.sin(x / float(width) * 2.0 * math.pi))
        # Draw text.
        draw.text((x, y), c, font=font, fill=255)
        # Increment x position based on chacacter width.
        charWidth, charHeight = draw.textsize(c, font=font)
        x += charWidth
    # Draw the image buffer.
    disp.image(image)
    disp.display()
    # Move position for next frame.
    pos += velocity
    # Start over if text has scrolled completely off left side of screen.
    if pos < -maxWidth:
        pos = startPos

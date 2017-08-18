
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image


# Raspberry Pi pin configuration:
RST = 24


# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# 128x64 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Load image based on OLED display height.  Note that image is converted to 1 bit color.
if disp.height == 64:
    image = Image.open('happycat_oled_64.ppm').convert('1')
else:
    image = Image.open('happycat_oled_32.ppm').convert('1')

# Alternatively load a different format image, resize it, and convert to 1 bit color.
#image = Image.open('happycat.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

# Display image.
disp.image(image)
disp.display()

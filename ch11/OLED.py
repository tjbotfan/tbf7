# coding: utf-8

import sys
import Adafruit_SSD1306
import time
# import Image
# import ImageDraw
# import ImageFont

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# argument
args = sys.argv
sel = args[1]
# Raspberry Pi pin configuration
RST = 1
# Initialise Libraly
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
# Misaki Font, awesome 8x8 pixel Japanese font, can be downloaded from the followig site$
# $ wget http://www.geocities.jp/littlimi/arc/misaki/misaki_ttf_2015-04-10.zip
font = ImageFont.truetype('/home/pi/font/misakifont/misaki_gothic.ttf', 8, encoding='unic')

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height

image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

if sel == '1':
        # Draw LED as an ellipse
        draw.ellipse((24, 1,32,10), outline=255, fill=0)
        # Draw face as a rectangle
        draw.rectangle((1, 6, 56, 46), outline=255, fill=0)
        # Draw eyes as ellipses
        draw.ellipse((13,34,20,42), outline=255, fill=0)
        draw.ellipse((37,34,44,42), outline=255, fill=0)
        # Draw Mouth as a polygon
        draw.polygon([(1,54), (56,51), (56,60), (1,63)], outline=255, fill=0)
        # Write text.
        top=10
        x=64
        draw.text((x, top),    u'こんにちは',  font=font, fill=255)
        draw.text((x, top+15), u'わたしは', font=font, fill=255)
        draw.text((x, top+30), u'TJBot zero', font=font, fill=255)
        draw.text((x, top+45), u'です', font=font, fill=255)
elif sel == '2':
        # Draw LED as an ellipse
        draw.ellipse((24, 1,32,10), outline=255, fill=255)
        # Draw a rectangle.
        # Draw face
        draw.rectangle((1, 6, 56, 46), outline=255, fill=255)
        # Draw an ellipse.
        # Draw eyes
        draw.ellipse((13,34,20,42), outline=255, fill=0)
        draw.ellipse((37,34,44,42), outline=255, fill=0)
        # Draw a polygon.
        # Draw Mouth
        draw.polygon([(1,54), (56,51), (56,60), (1,63)], outline=255, fill=255)
        # Write two lines of text.
        top=20
        x=64
        draw.text((x, top),    u'わたしと',  font=font, fill=255)
        draw.text((x, top+15), u'いっしょに', font=font, fill=255)
        draw.text((x, top+30), u'あそびましょう', font=font, fill=255)
elif sel == '3':
        image = Image.open('./TJBot_pic.jpg').resize((128, 64), Image.LANCZOS).convert("1")
else:
        sys.exit(1)
disp.image(image)
disp.display()
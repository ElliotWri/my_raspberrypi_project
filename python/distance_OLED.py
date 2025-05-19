import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from time import sleep
from datetime import datetime
from gpiozero import DistanceSensor

# Set up display
i2c = board.I2C()
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
small_font = ImageFont.truetype('FreeSans.ttf', 12)
large_font = ImageFont.truetype('FreeSans.ttf', 33)
disp.fill(0)
disp.show()

#Set up Sensor
sensor = DistanceSensor(echo=18, trigger=17)

# Make an image to draw on in 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

# Display a message on 3 lines, first line big font        
def display_message(top_line, line_2):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((0, 0),  top_line, font=large_font, fill=255)
    draw.text((0, 50),  line_2, font=small_font, fill=255)
    disp.image(image)
    disp.show()

while True:
    cm = sensor.distance * 100
    inch = cm / 2.5
    top_message = 'cm={:.1f}'.format(cm)
    bot_message = 'inches={:.1f}'.format(inch)
    display_message(top_message, bot_message)
    sleep(0.1)

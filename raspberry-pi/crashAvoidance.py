# type: ignore
import board
import digitalio
import time
import math
import pwmio
from adafruit_motor import servo
import adafruit_mpu6050
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio    

displayio.release_displays()

rled = digitalio.DigitalInOut(board.GP13)
rled.direction = digitalio.Direction.OUTPUT    # sets pin type
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP6)

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
while True:
    
    splash = displayio.Group() #creates display group

    title = "ANGULAR VELOCITY" #adds title block to display group
    text_area = label.Label(terminalio.FONT, text = title, color = 0xFFFF00, x = 5, y= 5) #sets font, text, color, and location
    splash.append(text_area) #adds to splash

    x_val = f"x: {round(mpu.acceleration[0], 3)}" #adds x value text block to display group and rounds it to 3 decimal places
    text_area = label.Label(terminalio.FONT, text = x_val, color = 0xFFFF00, x = 5, y = 16) #sets font, text, color, and location
    splash.append(text_area) #adds to splash

    y_val = f"y: {round(mpu.acceleration[1], 3)}" #adds y value text block to display group and rounds it to 3 decimal places
    text_area = label.Label(terminalio.FONT, text = y_val, color = 0xFFFF00, x = 5, y= 26) #sets font, text, color, and poition
    splash.append(text_area) #adds to splash

    z_val = f"z: {round(mpu.acceleration[2], 3)}" #adds z value text block to display group and rounds it to 3 decimal places
    text_area = label.Label(terminalio.FONT, text = z_val, color = 0xFFFF00, x = 5, y= 36) #sets font, text, color, and position
    splash.append(text_area) #adds to splash
    
    display.show(splash) #sends display group to OLED screen
    print(mpu.acceleration) #print values of acceleration
    time.sleep(0.2) #wait one second

    rled.value = False
    if 7.5 <= mpu.acceleration[0]:
        rled.value = True
        print("Unsafe rotation on X axis")
    if 7.5 <= mpu.acceleration[1]:
        rled.value = True
        print("Unsafe rotation on Y axis")
    if 2 <= mpu.acceleration[2]:
        rled.value = True
        print("Unsafe rotation on Z axis")
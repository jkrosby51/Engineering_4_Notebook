#type: ignore
import board
import digitalio
import pwmio
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

displayio.release_displays()

rled = digitalio.DigitalInOut(board.GP13)
rled.direction = digitalio.Direction.OUTPUT    # sets pin type
rled = True
sda_pin = board.GP16
scl_pin = board.GP17
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP6)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

splash = displayio.Group() #creates display group
hline = Line(0,32,128,32, color=0xFFFF00)

splash.append(hline)
hline = Line(64,0,64,64, color=0xFFFF00)
splash.append(hline)
circle = Circle(64, 32, 2, outline=0xFFFF00)
splash.append(circle)
display.show(splash)

def findArea(x1, y1, x2, y2, x3, y3):
    #print(f"({x1}, {y1}) ({x2}, {y2}) ({x3}, {y3})")
    area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2)
    return(area)

print("Welcome to the program!")
while True:
    splash = displayio.Group() #creates display group

    hline = Line(0,32,128,32, color=0xFFFF00)
    splash.append(hline)
    hline = Line(64,0,64,64, color=0xFFFF00)
    splash.append(hline)
    circle = Circle(64, 32, 2, outline=0xFFFF00)
    splash.append(circle)

    print("\nEnter all three points of a triangle")
    points = []
    try:
        userinput = input("Enter point #1 in format x,y: ")
        for a in userinput.split(","):
            points.append(float(a))
        userinput = input("Enter point #2 in format x,y: ")
        for a in userinput.split(","):
            points.append(float(a))
        userinput = input("Enter point #3 in format x,y: ")
        for a in userinput.split(","):
            points.append(float(a))
        for i in range(len(points)): print(int(points[i]))
        area = findArea(points[0], points[1], points[2], points[3], points[4], points[5])
        print(f"\nThe area of the triangle with points ({points[0]}, {points[1]}), ({points[2]}, {points[3]}), ({points[4]}, {points[5]}) is {area} square km.")
    
        text_area = label.Label(terminalio.FONT, text = f"{area}km2", color = 0xFFFF00, x = 5, y = 4) #sets font, text, color, and location
        splash.append(text_area) #adds to splash
        
        triangle = Triangle(int(points[0])+64, 32-int(points[1]), int(points[2])+64, 32-int(points[3]), int(points[4])+64, 32-int(points[5]), outline=0xFFFF00)
        splash.append(triangle)
    except:
        print("Invalid Syntax")

    

    display.show(splash) #sends display group to OLED screen
# type: ignore
import board
import digitalio
import time
import math
import pwmio
from adafruit_motor import servo

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# pin number (GP14 here) found on Pico Pin Map
rled = digitalio.DigitalInOut(board.GP14)
rled.direction = digitalio.Direction.OUTPUT    # sets pin type
gled = digitalio.DigitalInOut(board.GP15)
gled.direction = digitalio.Direction.OUTPUT
btn = digitalio.DigitalInOut(board.GP13)
btn.switch_to_input(pull=digitalio.Pull.DOWN)

pwm_servo = pwmio.PWMOut(board.GP2, duty_cycle=2 ** 15, frequency=50)
# pulse may need to be tuned to specific servo
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2200)

launched = True
print("Program Started")

while True:
    if btn.value:
        time.sleep(0.2)
        cdStart = time.monotonic()
        printedtimes = {}
        launched = True
        servo1.angle = 0
        gled.value = False
        print("Launch Countdown Starting")
        print("10")
        x = 9
        while x > 0:
            cdCurrent = time.monotonic() - cdStart
            if (math.floor(cdCurrent*10)/10) not in printedtimes:
                #print(math.floor(cdCurrent*10)/10)
                if (math.floor(cdCurrent*10)/10) == 0.0:
                    #print("rled ON")
                    # blinks on for half a second and then off for half a second, every second during the cooldown
                    rled.value = True
                if (math.floor(cdCurrent*10)/10) == 0.5:
                    #print("rled OFF")  
                    rled.value = False
                if (math.floor(cdCurrent*10)/10) >= 1.0:
                    print(x)
                    x = x - 1
                    cdStart = time.monotonic()
                    printedtimes = {}
                printedtimes[(math.floor(cdCurrent*10)/10)] = True
            if btn.value:                     # if you press the button during the for loop it will break the for loop, canceling the countdown
                launched = False
                x = -1
                rled.value = False
                print("ABORT")
                time.sleep(0.2)
        if launched and x == 0:
            rled.value = False
            gled.value = True
            print("Liftoff!")
            for angle in range(0, 180, 1):    # 180 - 0 degrees, -1º at a time.
                #print(angle)
                servo1.angle = angle

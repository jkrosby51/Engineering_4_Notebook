# type: ignore
import board
import digitalio
import time
import math
import pwmio
from adafruit_motor import servo

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

rled = digitalio.DigitalInOut(board.GP14)      # pin number (GP14 here) found on Pico Pin Map
rled.direction = digitalio.Direction.OUTPUT    # sets pin type
gled = digitalio.DigitalInOut(board.GP15)
gled.direction = digitalio.Direction.OUTPUT
btn = digitalio.DigitalInOut(board.GP13)
btn.switch_to_input(pull=digitalio.Pull.DOWN)

pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2200)   # pulse may need to be tuned to specific servo

launched = True

while True:
    if btn.value:
        time.sleep(0.2)
        cdStart  = time.time()
        printedtimes = {}
        launched = True
        gled.value = False
        print("Launch Countdown Starting")
        x = 10
        while x > 0:
            cdCurrent = time.time() - cdStart
            print(math.floor(cdCurrent*10)/10)
            
            if (math.floor(cdCurrent*10)/10) not in printedtimes:
                if (math.floor(cdCurrent*10)/10) == 0.0:
                    print("rled ON")
                    rled.value = True        # blinks on for half a second and then off for half a second, every second during the cooldown
                if (math.floor(cdCurrent*10)/10) == 0.5:
                    print("rled OFF")        #rled.value = False
                if (math.floor(cdCurrent*10)/10) > 1.0:
                    print("HI")
                    cdStart = time.time()
                    printedtimes = {}
                print((math.floor(cdCurrent*10)/10))
                printedtimes[(math.floor(cdCurrent*10)/10)] = True
            if btn.value:                     # if you press the button during the for loop it will break the for loop, canceling the countdown
                launched = False
                print("ABORT")
                time.sleep(0.2)
                
            
        if launched:
            gled.value = True
            print("Liftoff!");
            #for x in range(0.):              # 180 - 0 degrees, -1º at a time.
            #  servo1.angle = x
            #  time.sleep(0.05)

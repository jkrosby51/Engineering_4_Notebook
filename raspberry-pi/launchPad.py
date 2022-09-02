# type: ignore
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#LEDs will be implemented in the future
rled = digitalio.DigitalInOut(board.GP14)      # pin number (GP14 here) found on Pico Pin Map
rled.direction = digitalio.Direction.OUTPUT    # sets pin ype (output or input)
gled = digitalio.DigitalInOut(board.GP15)
gled.direction = digitalio.Direction.OUTPUT
btn = digitalio.DigitalInOut(board.GP13)
btn.switch_to_input(pull=digitalio.Pull.DOWN)

launched = False

while True:
    if btn.value:
        gled.value = False
        print("Launch Countdown Starting")
        for x in range(10):       # runs 10 times, from 0 to 9
            print(10-x)           # 10-x used to make the countdown go from 10 to 1
            rled.value = True     # blinks on for half a second and then off for half a second, every second during the cooldown
            time.sleep(0.5)       # var in seconds
            rled.value = False
            time.sleep(0.5)
            if btn.value:         # if you press the button during the for loop it will break the for loop, canceling the countdown
                launched = False
                break
                

            
        gled.value = True
        print("Liftoff!");
        #for x in range(18):    # 18 ticks of 0.05s and 5 degrees moved. Total of 90 degrees in 0.9 seconds.
        #  servo.angle = servo.angle + 5     !!! psuedo code, will be correctly implemented in the future !!!
        #  time.sleep(0.05)
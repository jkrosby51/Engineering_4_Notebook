# type: ignore
import board
import digitalio
import time
import math
import pwmio
from adafruit_motor import servo
import adafruit_mpu6050
import busio

rled = digitalio.DigitalInOut(board.GP13)
rled.direction = digitalio.Direction.OUTPUT    # sets pin type
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    #print(f"x: {mpu.acceleration[0]}m/s2 y: {mpu.acceleration[1]}m/s2 z: {mpu.acceleration[2]}m/s2")
    time.sleep(0.1)
    rled.value = False
    if 7.5 <= mpu.acceleration[0] <= 11.5:
        rled.value = True
        print("Unsafe rotation on X axis")
    if 7.5 <= mpu.acceleration[1] <= 11.5:
        rled.value = True
        print("Unsafe rotation on Y axis")
    if -2 <= mpu.acceleration[2] <= 2:
        rled.value = True
        print("Unsafe rotation on Z axis")
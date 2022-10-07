#type: ignore
import time
import board
import digitalio
import pwmio
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
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

splash = displayio.Group() #creates display group

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

# The Morse code timing rules we will use for signaling are: 
# a dot (.) lasts for 1/4 second. a dash (-) lasts for 3/4 seconds. 
# the space between dots and dashes that are part of the same letter is 1/4 second.
# space between letters is 3/4 seconds
# space between words is 1+3/4 seconds

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

print("Welcome to the program! Enter '-q' at any time to quit")

while True:
    userInput = input("Input your string: ")
    ans = ""
    if userInput == "-q": break
    for letter in userInput:
        if letter != ' ':
            ans = ans + MORSE_CODE[letter.upper()] + " "
        else: ans = ans + " / "
    print()
    print(ans)
    #text_area = label.Label(terminalio.FONT, text = f"{ans}", color = 0xFFFF00, x = 5, y = 32) #sets font, text, color, and location
    #splash.append(text_area) #adds to splash

    for letter in userInput:
        #print(f"{letter} -> {MORSE_CODE[letter.upper()]}")
        if(letter != " "):
            for sandwhich in MORSE_CODE[letter.upper()]:
                if MORSE_CODE[letter.upper()] == ".": 
                    rled.value = True
                    time.sleep(dot_time)
                elif MORSE_CODE[letter.upper()] == "-": 
                    rled.value = True
                    time.sleep(dash_time)
                rled.value = False
        if letter == " ": time.sleep(between_words)
        else: time.sleep(between_letters)

        #
        #   Somethin is a bit wonky in here for loop. (skipping dots/dashes? check everything!)
        #

    display.show(splash) #sends display group to OLED screen

print("Have a good day!")
splash = displayio.Group()
text_area = label.Label(terminalio.FONT, text = "Goodbye.", color = 0xFFFF00, x = 5, y = 32) #sets font, text, color, and location
splash.append(text_area) #adds to splash
display.show(splash) #sends display group to OLED screen
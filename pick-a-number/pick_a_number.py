from machine import Pin
from keypad import Keypad
from gpio_lcd import GpioLcd
import utime
import random

# initialise components
keypad_rows = [9, 8, 7, 6]
keypad_cols = [3, 2, 1, 0]

keypad = Keypad(keypad_rows, keypad_cols)

screen = GpioLcd(rs_pin=Pin(15), enable_pin=Pin(14),
              d4_pin=Pin(13), d5_pin=Pin(12),
              d6_pin=Pin(11), d7_pin=Pin(10))

        
screen.scroll_text("Welcome to the Challenge of Wits!")
utime.sleep(1)
screen.scroll_text("Press any key to begin")
keypad.get_keypress()

while True:
    screen.clear()
    screen.putstr("Pick a number")
    screen.move_to(0,1)
    screen.putstr("From 0-9")
    answer = random.randrange(0, 10)
    utime.sleep(1)
    guess = keypad.get_keypress()
    screen.clear()
    if guess == str(answer):
        screen.putstr("Congratulations!")
        screen.move_to(0,1)
        screen.putstr("You won!")
    else:
        screen.putstr("Womp womp!")
        screen.move_to(0,1)
        screen.putstr("You lost.")
        
    utime.sleep(2)
    screen.clear()
    screen.putstr("Try again?")
    screen.move_to(0,1)
    screen.putstr("Press any key")
    keypad.get_keypress()
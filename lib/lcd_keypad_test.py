from machine import Pin
import utime
from gpio_lcd import GpioLcd
from keypad import Keypad

screen = GpioLcd(rs_pin=Pin(15), enable_pin=Pin(14),
              d4_pin=Pin(13), d5_pin=Pin(12),
              d6_pin=Pin(11), d7_pin=Pin(10))

keypad_rows = [9, 8, 7, 6]
keypad_cols = [3, 2, 1, 0]

keypad = Keypad(keypad_rows, keypad_cols)


while True:
    screen.clear()
    screen.putstr("Press a key: ")
    screen.blink_cursor_on()
    utime.sleep(1)
    key = keypad.get_keypress()
    screen.blink_cursor_off()
    screen.clear()
    screen.putstr("You pressed: ")
    screen.putstr(key)
    utime.sleep(1)
    screen.clear()
    screen.putstr("Press * ")
    screen.move_to(0,1)
    screen.putstr("to go again")
    key = keypad.get_keypress()
    while key != '*':
        key = keypad.get_keypress()

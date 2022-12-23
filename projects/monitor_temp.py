import machine
import utime
import dht
from keypad import Keypad
from gpio_lcd import GpioLcd


# Initialise components
keypad_rows = [9, 8, 7, 6]
keypad_cols = [3, 2, 1, 0]

keypad = Keypad(keypad_rows, keypad_cols)

screen = GpioLcd(rs_pin=Pin(15), enable_pin=Pin(14),
              d4_pin=Pin(13), d5_pin=Pin(12),
              d6_pin=Pin(11), d7_pin=Pin(10))

sensor = dht.DHT11(machine.Pin(4))
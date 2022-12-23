from machine import Pin
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

sensor = dht.DHT11(Pin(4))


# Define menu and sensor reading functions
def display_readings(option):
    sensor.measure()
    if option == 'A':
        screen.clear()
        screen.putstr("Temp: {} Hum: {}".format(sensor.temperature(),
                                                sensor.humidity()))
    elif option == 'B':
        screen.clear()
        screen.putstr("Temp: {}".format(sensor.temperature()))
    elif option == 'C':
        screen.clear()
        screen.putstr("Humidity: {}".format(sensor.humidity()))


def menu(keypress):
    menu_text = "Press A for temp and humidity, B for temp only, C for humidity only"
    if keypress == '*':
        screen.scroll_text(menu_text)
    elif keypress in "ABC":
        display_readings(keypress)
    else:
        screen.scroll_text("Unknown option selected. Press * to view menu options again.")


# Display welcome text
screen.clear()
screen.scroll_text("Welcome to the Temperature Monitoring Program.")
utime.sleep(1)
screen.scroll_text("Press * to view menu options.")
utime.sleep(1)


# Enter main code loop
while True:
    screen.move_to(0,1)
    screen.putstr("Press * for menu")
    menu(keypad.get_keypress())
    
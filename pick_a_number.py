"""Pick a number game, using keypad to receive
user input and lcd screen to display outcome.
"""

import machine
import utime
import gpio_lcd

# two lists of gpio numbers
def InitKeypad(rows, cols):
    row_pins = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in rows]
    col_pins = [machine.Pin(pin_num, machine.Pin.IN, pull=machine.Pin.PULL_DOWN) for pin_num in cols]
    
    for row in range(4):
        row_pins[row].low()
    
# pass to timer init call        
def PollKeypad(timer):
    # definitions
    KEY_UP = const(0)
    KEY_DOWN = const(1)

    keys = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'],
            ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]
    key = None

    for row in range(4):
        row_pins[row].high()
        for col in range(4):
            if col_pins[col].value() == KEY_DOWN:
                key = KEY_DOWN
            else:
                key = KEY_UP
            if key == KEY_DOWN:
                lcd_print(keys[row][col])
                
lcd = gpio_lcd.GpioLcd(rs_pin=machine.Pin(15),
              enable_pin=machine.Pin(14),
              d4_pin=machine.Pin(13),
              d5_pin=machine.Pin(12),
              d6_pin=machine.Pin(11),
              d7_pin=machine.Pin(10),
              num_lines=2, num_columns=16)


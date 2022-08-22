"""Basic program to test lcd screen and keypad working
together."""

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
                


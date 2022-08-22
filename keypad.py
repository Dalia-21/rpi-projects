import machine
import utime

keys = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]

rows = [6,7,8,9]
cols = [2,3,4,5]

row_pins = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in rows]
col_pins = [machine.Pin(pin_num, machine.Pin.IN, pull=machine.Pin.PULL_DOWN) for pin_num in cols]

led = machine.Pin(25, machine.Pin.OUT)

timer_one = machine.Timer()
timer_two = machine.Timer()

KEY_UP = const(0)
KEY_DOWN = const(1)

def BlinkLED(timer):
    led.toggle()
    
def InitKeypad():
    for row in range(4):
        row_pins[row].low()
            
def PollKeypad(timer):
    key = None
    for row in range(4):
        row_pins[row].high()
        for col in range(4):
            if col_pins[col].value() == KEY_DOWN:
                key = KEY_DOWN
            else:    
                key = KEY_UP
            if key == KEY_DOWN:
                print(keys[row][col])
                last_key_press = keys[row][col]
        row_pins[row].low()
                
                
InitKeypad()

timer_one.init(freq=5, mode=machine.Timer.PERIODIC, callback=BlinkLED)
timer_two.init(freq=2, mode=machine.Timer.PERIODIC, callback=PollKeypad)
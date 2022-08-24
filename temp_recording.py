"""This project reads the temperature and humidity from
a DHT11 sensor and displays it on an lcd screen. A keypad
can be used to control the lcd output and the values are
written to a file every ten minutes.
The wiring which was used for this project was adapted in part
from the diagram at
https://circuitbasics.com/raspberry-pi-lcd-set-up-and-programming-
in-python/
"""

import machine
import utime
import gpio_lcd
import dht
import _thread


# initialise keypad pins
cols = [6,7,8,9]
rows = [0,1,2,3]

row_pins = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in rows]
col_pins = [machine.Pin(pin_num, machine.Pin.IN, pull=machine.Pin.PULL_DOWN) for pin_num in cols]
    
for row in range(4):
    row_pins[row].low()
    
    
# pass to timer init call        
def PollKeypad(timer):
    global last_write_time
    global sensor
    
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
                ProcessInput(keys[col][row])
                
    if utime.time() - last_write_time >= 600:
        sensor.measure()
        sensor_file = open('temps.dat', 'a')
        sensor_file.write(" ".join(str(utime.time(), sensor.temperature(), sensor.humidity()), "\n"))
        sensor_file.close()
        last_write_time = utime.time()


def ProcessInput(key):
    global sensor
    global blinking
    
    if key == '*':
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr('Menu *-menu,D-Bl')
        lcd.move_to(0,1)
        lcd.putstr('A-all,B-T,C-H')
    elif key == 'A':
        sensor.measure()
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr('Temp: {}'.format(sensor.temperature()))
        lcd.move_to(0,1)
        lcd.putstr('Humidity: {}'.format(sensor.humidity()))
    elif key == 'B':
        sensor.measure()
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr('Temp: {}'.format(sensor.temperature()))
    elif key == 'C':
        sensor.measure()
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr('Humidity: {}'.format(sensor.humidity()))
    elif key == 'D':
        if blinking == False:
            blinking = True
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr('Now blinking')
            _thread.start_new_thread(toggle_blink, ())
            utime.sleep(1)
            lcd.clear()
            lcd.move_to(2,0)
            lcd.putstr('Press keypad')
            lcd.move_to(2,1)
            lcd.putstr('for options')
        else:
            blinking = False
    else:
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr('Unknown Input')
        lcd.move_to(0,1)
        lcd.putstr('Press * for menu')
        
        
def toggle_blink():
    global led
    global blinking
    while blinking:
        led.value(1)
        utime.sleep_ms(500)
        led.value(0)
        utime.sleep_ms(500)
    
lcd = gpio_lcd.GpioLcd(rs_pin=machine.Pin(15),
              enable_pin=machine.Pin(14),
              d4_pin=machine.Pin(13),
              d5_pin=machine.Pin(12),
              d6_pin=machine.Pin(11),
              d7_pin=machine.Pin(10),
              num_lines=2, num_columns=16)

led = machine.Pin(25,machine.Pin.OUT)
blinking = False

sensor = dht.DHT11(machine.Pin(4))

last_write_time = utime.time()

stop_button = machine.Pin(16,machine.Pin.IN,machine.Pin.PULL_DOWN)

def StopIRQHandler(pin):
    global led
    
    led.value(1)
    while True:
        pass
    
stop_button.irq(trigger = machine.Pin.IRQ_RISING,
                handler = StopIRQHandler)

lcd.clear()
lcd.move_to(0,0)
lcd.putstr('Temp Monitoring')
lcd.move_to(0,1)
lcd.putstr('In 3...')
utime.sleep(1)
lcd.move_to(3,1)
lcd.putchar('2')
utime.sleep(1)
lcd.move_to(3,1)
lcd.putchar('1')
utime.sleep(1)
lcd.clear()
lcd.move_to(0,0)
lcd.putstr('Press * for menu')

keypad_timer = machine.Timer()

keypad_timer.init(freq=2, mode=machine.Timer.PERIODIC, callback=PollKeypad)

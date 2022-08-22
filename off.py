"""This is a simple utility for setting all Raspberry Pi Pico
pins to 0, turning everything off."""

import machine

for pin_num in range(0,23):
    pin = machine.Pin(pin_num, machine.Pin.OUT)
    pin.value(0)
    
for pin_num in range(25,29):
    pin = machine.Pin(pin_num, machine.Pin.OUT)
    pin.value(0)

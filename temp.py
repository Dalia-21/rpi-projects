"""Most basic test of a DHT11 sensor using inbuilt library."""

import dht
import machine
import utime

d = dht.DHT11(machine.Pin(4))

while True:
    d.measure()
    print("Temp: ", d.temperature())
    print("Humidity: ", d.humidity())
    utime.sleep(1)

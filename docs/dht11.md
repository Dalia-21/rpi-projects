# DHT 11
This module for measuring temperature and humidity is simple to set up and use.
## Wiring
On the module I have, the pins are clearly marked on the module. One goes to ground, one goes to power, which I have connected to the ```VBUS``` pin on the Raspberry Pi Pico, which is nominally 5V,and one gets connected to a GPIO pin.
## Code
The code for reading the device values is also simple. To begin with, the dht module built into the board's version of Micropython needs to be imported. The relevant imports are

```
import machine
import dht
```

An instance of the DHT11 object then needs to be created, with

```
sensor = dht.DHT11(machine.Pin(4))
```

4 is the number of the GPIO pin I have connected the sensor to. This number should be changed as appropriate. The dht module only needs to receive the pin; no mode needs to be specified.
Setup is now complete, and the device can be measured from. Begin by reading from the device, with

```
sensor.measure()
```

This takes a reading, but returns no values. The methods for returning the values are

```
sensor.temperature()
sensor.humidity()
```

These values can be printed to console, displayed on a screen, or stored in a variable for later use.

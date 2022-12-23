# Keypad
The module for receiving user input from a matrix keypad requires wires connected to the rows and columns of the matrix. The Pico reads from the matrix by powering the rows, one at a time, and then checking each of the column pins to see if a circuit has been completed. This is checked in a very short period of time, so it is recommended to run this check every few milliseconds until a keypress has been identified, or a certain length of time has elapsed. The ```keypad.py``` file implements the code required for using this device.
## Wiring
Wiring is very simple, at least for the 4x4 keypad I use. Four wires must be connected to GPIO pins going to the row side of the keypad, and four wires must be connected to GPIO pins going to the column side.
## Code
The class constructor for this module has two positional arguments and one optional one. The required arguments are ```rows``` and ```cols```, both lists, which must contain the pin numbers corresponding to the pin numbers which have been plugged in on the Pico device. Care must be taken to provide the pin numbers in descending order, as this is the order in which rows and columns are read from the keypad. Alternatively, a custom keys list can be provided, with the key values in reverse order. If this is not observed, the wrong string values will be returned for each keypress. Initialisation of the pins is performed automatically, and a method is provided for constantly polling the keypad. The method returns a string containing the value of the key which was pressed. Setup and testing of the module is as simple as the following snippet:

```
python
>>>from keypad import Keypad
>>>rows = [9,8,7,6]
>>>cols = [3,2,1,0]
>>>test_keypad = Keypad(rows, cols)
>>>print(test_keypad.get_keypress())
'A'
>>>
```

By default the class supports a 3x3 matrix, with keys 1 through 9, and a 4x4 matrix with keys 1 through 9 and letters A through D. The format is determined by the number of pins provided. If a non supported matrix is provided, a custom keys list must be provided, otherwise the keys will be set to ```None``` and the program will enter a failed state, indicated by a flashing LED. The keys list can be provided as an optional argument to the class constructor. The ```get_keypress()``` method can also be provided an optional argument with a timeout. After the number of seconds specified, if no key has been pressed, the method will return ```None```.

import machine
import utime
import time


class Keypad:
    
    def __init__(self, rows, cols, keys=None):
        """User must pass in two valid lists of row and column pin numbers
        and a matching nested list of key string values if these do not match.
        the default values for 3x3 and 4x4 keypads provided.
        If this is not done, the keys will be set to None and the program will
        fail when a key is pressed, since no error handling is possible for the Pico.
        One option for the user would be to check if the keys are set to None and
        to enable a blinking LED if this is the case.
        NOTE: pin numbers should be given in descending order, as this is the order
        that the key matrix checks in, otherwise provide a custom key list with
        reversed key order."""

        if keys:
            self.keys = keys
        else:
            if len(rows) == 3 and len(cols) == 3:
                self.keys = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            elif len(rows) == 4 and len(cols) == 4:
                self.keys = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], \
                             ['7', '8', '9', 'C'], ['*', '0', '#', 'D']]
            else:
                self.keys = None

        self.rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in rows]
        self.cols = [machine.Pin(pin_num, machine.Pin.IN, pull=machine.Pin.PULL_DOWN) \
                     for pin_num in cols]
        
        # Using range on these values to initialise pins will give the correct length
        self.row_length = len(self.rows)
        self.col_length = len(self.cols)
        
        # Delay between keypad polls
        self.delay_val = 0.02
        
        
        # Turn all pins off at start of program
        for row in range(self.row_length):
            self.rows[row].low()
            
        
    def _poll_keypad(self):
        key = None
        for row in range(self.row_length):
            self.rows[row].high()
            for col in range(self.col_length):
                if self.cols[col].value():
                    key = self.keys[row][col]
            self.rows[row].low()
        return key
    
    
    def get_keypress(self, timeout=None):
        """Keep polling keypad until timeout is reached or forever.
        Poll repeats after delay value."""
        if timeout:
            start_time = time.time()
            while time.time() - start_time < timeout:
                key_val = self._poll_keypad()
                if key_val:
                    return key_val
                utime.sleep(self.delay_val)
        else:
            while True:
                key_val = self._poll_keypad()
                if key_val:
                    return key_val
                utime.sleep(self.delay_val)

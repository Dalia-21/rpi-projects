# Monitor Temperature
This is a small program for monitoring temperature using a DHT 11 module. The data is not stored, but instead simply displayed on an LCD screen. A keypad allows for displaying different menu options and selecting either temperature, humidity, or both.
## Setup
Setup for this program is very simple. The program makes use of the keypad and LCD modules seen in other projects. These must be initialised, as must the dht sensor. Details of initialisation are further explained in the ```docs``` for this repository.
## Main Code Loop
After displaying a welcome text, the program enters a menu, where the user can select from several options. When the user chooses to view the menu, a scrolling text displays the options. The other options are to view temperature, humidity or both, at which point the sensor will be read from, as explained in the documentation for the dht module.

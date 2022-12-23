# Pick A Number
This is a small program which implements a number guessing game on the Raspberry Pi Pico. It makes use of the modules for the keypad and LCD screen, found in the ```lib``` folder.
## Behaviour
At the beginning of runtime, the program displays a welcome message to the screen. After a short delay, the screen displays a prompt to pick a number from 0 to 9. The program simultaneously chooses a random number. Once the user has selected a number, the program will announce the result. The user will then be given the option to play again.
## Code
The first section of the file simply initialises the keypad and screen objects. The welcome message is then displayed, before the program enters the main loop, allowing the player to play against the machine an infinite number of times.

# TrinkeyMouseTwiddler
A Circuit Python version of The MouseTwiddler

# Setting it up on a new Trinkey
- Insert the trinkey into a spare USB port on your computer
- carefully double click the small reset button on the trinkey <br>
    Its between the 4 Neopixel Leds and the SAMD chip itself<br>
    This will make a drive appear called TrinkeyBoot.
- copy the file in CircuitPythonBIOS (a UF2 file) to this TrinkeyBoot volume
- The Trinkey's leds will flash red and TrinkeyBoot will disappear<br>
    Replaced by a volume called CircuitPy.
- To CircuitPy copy the lib folder and the code.py file
- The Trinkey will start twiddling the mouse every 30 seconds<br>
    allong with the neopixeld changing colors...
    

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
    along with the neopixeld changing colors...

If you want to use an alternate blinking pattern...

- Rename the code.py file to something else.
- Rename the the AlternateBlinky.py file to code.py
- Eject the CircuitPy volume using your OS Spectific mechanisim.
    - On the MAC is right click and select eject on the context menu
    - On windows the USB icon in your taskbar will have options to safely remove the volume
- Remove and re-insert your trinkey to run the now code...

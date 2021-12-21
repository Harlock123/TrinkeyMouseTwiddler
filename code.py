import usb_hid
import time
import board
import neopixel
from adafruit_hid.mouse import Mouse

# pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

p1 = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=0.1, auto_write=False)
m = Mouse(usb_hid.devices)

modulo = 0

while True:

    if modulo == 0:
        p1[0] = (255, 0, 0)
        p1[1] = (0, 255, 0)
        p1[2] = (0, 0, 255)
        p1[3] = (0, 0, 0)

    if modulo == 3:
        p1[3] = (255, 0, 0)
        p1[0] = (0, 255, 0)
        p1[1] = (0, 0, 255)
        p1[2] = (0, 0, 0)

    if modulo == 2:
        p1[2] = (255, 0, 0)
        p1[3] = (0, 255, 0)
        p1[0] = (0, 0, 255)
        p1[1] = (0, 0, 0)

    if modulo == 1:
        p1[1] = (255, 0, 0)
        p1[2] = (0, 255, 0)
        p1[3] = (0, 0, 255)
        p1[0] = (0, 0, 0)

    p1.show()

    modulo = modulo + 1

    if modulo == 5:
        modulo = 0

    time.sleep(30)

    m.move(2, 0)
    time.sleep(0.1)
    m.move(0, 2)
    time.sleep(0.1)
    m.move(-2, 0)
    time.sleep(0.1)
    m.move(0, -2)
    time.sleep(0.1)

    # pixels.fill((255, 0, 0))
    # time.sleep(0.5)
    # pixels.fill((0, 0, 0))
    # time.sleep(0.5)

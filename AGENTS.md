# AGENTS.md

Notes for anyone, human or AI agent, changing this code. `README.md` covers putting the firmware and code on a
new Trinkey; this file covers what the code does and how to change it safely.

## What this is

A CircuitPython "mouse twiddler" for the Adafruit NeoPixel Trinkey M0. The board appears to the computer as a USB
mouse and nudges the pointer in a tiny square now and then (so the computer does not go idle), while its four
NeoPixels show colour patterns. It runs only on the Trinkey under CircuitPython, not on a desktop Python.

## Commands

There is nothing to build and there are no tests. To deploy:

- Put the board in bootloader mode (double-click reset) and copy the `.uf2` from `CircuitPythonBIOS/` to the
  `TrinkeyBoot` drive. This installs CircuitPython 7.0.0.
- Copy `lib/` and `code.py` to the `CIRCUITPY` drive. CircuitPython runs `code.py` at start-up and again
  whenever it is saved.

## Layout

- `code.py`: the default program. Every 0.25 s it rotates four colours round the NeoPixels (at brightness 0.05).
  After 30 counts of 1.25 s each (37.5 s, plus 0.4 s for the move itself: about 38 s) it moves the mouse right,
  down, left and up by 2 pixels.
- `AlternateBlinky.py`: a quieter pattern. The LEDs stay dark, and every 30 s it moves the mouse in the same small
  square while flashing the LEDs once. Rename it to `code.py` on the board to use it.
- `lib/`: the compiled CircuitPython libraries the scripts import: `adafruit_hid` (only `mouse.mpy`),
  `neopixel.mpy` and `adafruit_pixelbuf.mpy`.
- `CircuitPythonBIOS/`: the CircuitPython 7.0.0 firmware for the NeoPixel Trinkey M0.

## Rules that keep it working

- **Libraries must match the firmware.** `.mpy` files are compiled for a CircuitPython major version; if you
  change the `.uf2` to a newer CircuitPython, replace `lib/` with the matching library bundle too.
- **Keep `lib/` small.** The Trinkey M0 has very little flash; copy in only the modules the code imports.
- **Keep the movements balanced.** Each cycle moves the mouse out and back by the same amounts, so the pointer
  ends where it started. Keep it that way if you change the pattern.
- **Hardware names.** `board.NEOPIXEL` drives the four LEDs and `usb_hid.devices` the USB mouse.

## Making a change

- Edit the script, copy it to the board as `code.py`, and watch the LEDs and the pointer. Save it with plain LF
  line endings, as the existing files are.
- If the timing or the setup steps change, update `README.md`.

There is no CI workflow in this repository.

#! /usr/bin/python3

import os
import sys

import logging
import threading
import time

import random

from rpi_ws281x import PixelStrip, Color
from getkey import getkey, keys

# LED strip configuration:
LED_COUNT = 16        # Number of LED pixels.
LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 125  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
     # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    colorWipe(strip, Color(0, 0, 0), 10)
    try:
        while True:
            key = getkey()
            led_id = random.randint(0, 16)
            red = random.randint(0, 255)
            blue = random.randint(0, 255)
            green = random.randint(0, 255)
            logging.info("key '%s'", key)
            logging.info("led_id %d", led_id)
            logging.info("red %d, blue %d green %d", red, blue, green)
            logging.info("Enabling led")
            colorWipe(strip, Color(red, blue, green), 10)
            time.sleep(1)
            colorWipe(strip, Color(0, 0, 0), 10)
            logging.info("Disabling led")

    except SyntaxError:
        pass

    colorWipe(strip, Color(0, 0, 0), 10)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

    sys.exit()

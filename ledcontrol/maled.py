# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import random

from neopixel import *

# LED strip configuration:
LED_COUNT = 60  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
FULL_COLOR = 255 # maximum brightness of one rgb color part

def getrandcolorvalue(brightness, a, b):
    return brightness * random.randint(a, b)


def getrandomcolor(red, green, blue, a, b):
    return (getrandcolorvalue(red, a, b), getrandcolorvalue(green, a, b), getrandcolorvalue(blue, a, b))


def meteor(strip, r, g, b, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, getrandomcolor(r, g, b, 0.9, 1))
        strip.setPixelColor(i+1, getrandomcolor(r, g, b, 1, 1))
        strip.setPixelColor(i+2, getrandomcolor(r, g, b, 0.95, 1))
        strip.setPixelColor(i+3, getrandomcolor(r, g, b, 0.9, 0.95))
        strip.setPixelColor(i+3, getrandomcolor(r, g, b, 0.9, 0.95))
        strip.setPixelColor(i+3, getrandomcolor(r, g, b, 0.8, 0.95))
        strip.setPixelColor(i+6, getrandomcolor(r, g, b, 0.7, 0.9))
        strip.setPixelColor(i+7, getrandomcolor(r, g, b, 0.6, 0.85))
        strip.setPixelColor(i+8, getrandomcolor(r, g, b, 0.6, 0.7))
        strip.setPixelColor(i+9, getrandomcolor(r, g, b, 0.5, 0.7))
        strip.setPixelColor(i+10, getrandomcolor(r, g, b, 0.4, 0.6))
        strip.setPixelColor(i+11, getrandomcolor(r, g, b, 0.3, 0.5))
        strip.setPixelColor(i+12, getrandomcolor(r, g, b, 0.2, 0.4))
        strip.setPixelColor(i+13, getrandomcolor(r, g, b, 0.1, 0.3))
        strip.setPixelColor(i+14, getrandomcolor(r, g, b, 0, 0.2))
        strip.setPixelColor(i+15, getrandomcolor(r, g, b, 0, 0.2))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def lasssprudeln(strip, r, g, b, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, (r, g, b))
        strip.setPixelColor(i+1, (r*0.8, g*0.8, b*0.8))
        strip.setPixelColor(i+2, (r*0.7, g*0.7, b*0.7))
        strip.setPixelColor(i+3, (r*0.6, g*0.6, b*0.6))
        strip.setPixelColor(i+4, (r*0.4, g*0.4, b*0.4))
        strip.setPixelColor(i+4, (r*0.2, g*0.2, b*0.4))
        strip.setPixelColor(i+4, (r*0, g*0, b*0))
        strip.show()
        time.sleep(wait_ms / 1000.0)


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print 'Press Ctrl-C to quit.'
    while True:
        lasssprudeln(strip, 255, 255, 255)

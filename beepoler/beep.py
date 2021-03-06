#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

BeepPin = 11  # pin11
dummy = 0


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(BeepPin, GPIO.OUT)  # Set BeepPin's mode is output
    GPIO.output(BeepPin, GPIO.HIGH)  # Set BeepPin high(+3.3V) to off beep


def loop():
    while True:
        if dummy == 1:
            GPIO.output(BeepPin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(BeepPin, GPIO.HIGH)
            time.sleep(0.1)
        else:
            time.sleep(0.4)


def destroy():
    GPIO.output(BeepPin, GPIO.HIGH)  # beep off
    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    print 'Press Ctrl+C to end the program...'
    setup()
    try:
        loop()

        for line in sys.stdin:
            if line == "ON":
                GPIO.output(BeepPin, GPIO.LOW)
                dummy = 1
            else:
                GPIO.output(BeepPin, GPIO.HIGH)
                dummy = 0

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

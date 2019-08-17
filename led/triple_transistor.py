#!/usr/bin/env python3
"""Turning a LED on/off with 5V input voltage with a NPN-transistor"""

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class LED:
    """Creating a LED, mapping it and turning it on/off"""
    def __init__(self, PIN):
        self.pin, self.inout = PIN, GPIO.OUT
        GPIO.setup(self.pin, self.inout)
    def turn_on(self):
        """Turning on the LED"""
        GPIO.output(self.pin, GPIO.LOW)
    def turn_off(self):
        """Turning off the LED"""
        GPIO.output(self.pin, GPIO.HIGH)
#configuration
FIRST = LED(11)
SECOND = LED(13)
THIRD = LED(15)
#program
try:
    while True:
        print("LED ON")
        FIRST.turn_on()
        sleep(0.5)
        SECOND.turn_on()
        sleep(0.5)
        THIRD.turn_on()
        sleep(1)
        print("LED OFF")
        FIRST.turn_off()
        sleep(0.5)
        SECOND.turn_off()
        sleep(0.5)
        THIRD.turn_off()
        sleep(1)
except KeyboardInterrupt:
    print("Programm canceled through KeyInterrupt.")
finally:
    print("Cleaning up...")
    GPIO.cleanup()
print("Finished script!")

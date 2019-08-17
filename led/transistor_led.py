#!/usr/bin/env python3
"""Turning a LED on/off with 5V input voltage with a NPN-transistor"""

from time import sleep
import RPi.GPIO as GPIO

BASEPIN = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BASEPIN, GPIO.OUT)
try:
    while True:
        print("LED ON")
        GPIO.output(BASEPIN, GPIO.HIGH)
        sleep(1)
        print("LED  OFF")
        GPIO.output(BASEPIN, GPIO.LOW)
        sleep(1)
except KeyboardInterrupt:
    print("Programm canceled through KeyInterrupt.")
finally:
    print("Cleaning up...")
    GPIO.cleanup()
print("Finished script!")

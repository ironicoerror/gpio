#!/usr/bin/env python3
"""Turning a LED on/off with 5V input voltage with a NPN-transistor"""

from time import sleep
import RPi.GPIO as GPIO

BASEPIN = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(BASEPIN, GPIO.OUT)

print("LED ON")
GPIO.output(BASEPIN, GPIO.HIGH)
sleep(1)
print("LED  OFF")
GPIO.output(BASEPIN, GPIO.LOW)
GPIO.cleanup()

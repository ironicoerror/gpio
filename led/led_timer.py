#!/usr/bin/env python3
"""turning on an LED and turn it off again after sleep"""

from time import sleep
import RPi.GPIO as GPIO

PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

print("LED ON")
GPIO.output(PIN, GPIO.HIGH)
sleep(1)
print("LED  OFF")
GPIO.output(PIN, GPIO.LOW)
GPIO.cleanup()

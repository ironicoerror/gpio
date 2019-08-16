#!/usr/bin/env python3
"""Turning an LED on as long as the switch is pressed"""

from time import sleep
import RPi.GPIO as GPIO

OUTPIN = 18
SWITCHPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPIN, GPIO.OUT)
GPIO.setup(SWITCHPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    SWITCHVALUE = GPIO.input(SWITCHPIN)
    if  SWITCHVALUE != 0:
        print("LED ON")
        GPIO.output(OUTPIN, GPIO.HIGH)
        sleep(0.5)
    else:
        GPIO.output(OUTPIN, GPIO.LOW)
GPIO.cleanup()

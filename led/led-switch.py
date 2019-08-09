#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


while True:
    switchvalue = GPIO.input(21)
    if  switchvalue != 0:
        print("LED ON")
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.5)
    else:
        GPIO.output(18, GPIO.LOW)

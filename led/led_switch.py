#!/usr/bin/env python3
"""Turning an LED on as long as the switch is pressed"""

import RPi.GPIO as GPIO

OUTPIN = 15
SWITCHPIN = 21
GPIO.setmode(GPIO.BOARD)
GPIO.setup(OUTPIN, GPIO.OUT)
GPIO.setup(SWITCHPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
status = True
def switch_led_status(channel):
    """detects if the LED is on or off and turns it into the complement"""
    print("Rising signal on pin " + str(channel))
    global status
    status = not status
    GPIO.output(OUTPIN, status)

try:
    GPIO.add_event_detect(SWITCHPIN, GPIO.RISING,\
         callback=switch_led_status, bouncetime=200)
    while True:
        pass
except KeyboardInterrupt:
    print("Programm canceled through KeyInterrupt.")
finally:
    print("Cleaning up...")
    GPIO.cleanup()
print("Finished script!")

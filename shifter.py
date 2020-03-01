#!/usr/bin/python3
input_pins ={
'serial': 18,
'rclk': 19,
'srclr': 20,
'srclk': 21,
'status': 12
}
import RPi.GPIO as GP
from time import sleep
from random import randint

#init gpio
GP.setmode(GP.BCM)
for pins in input_pins:
    GP.setup(input_pins[pins], GP.OUT)
#functions
def pulse(pin):
    GP.output(pin, 0)
    GP.output(pin, 1)
    GP.output(pin, 0)
#start programm
GP.output(input_pins['status'], 1)
GP.output(input_pins['srclr'], 1)
count = 0
while True:
    try:
        count += 1
        if count % 2 != 0:
            ser_input = 1
        else: ser_input = 0
        for i in range(8):
#            ser_input = randint(0, 1)
            GP.output(input_pins['serial'], ser_input)
            pulse(input_pins['srclk'])
            pulse(input_pins['rclk'])
            sleep(0.1)
    except KeyboardInterrupt:
        print("Programm wird beendet")
        break
#finish and reset
GP.output(input_pins['srclr'], 0)
pulse(input_pins['rclk'])
GP.output(input_pins['status'], 0)
GP.cleanup()


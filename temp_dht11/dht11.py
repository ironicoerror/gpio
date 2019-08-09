#! /usr/bin/env python3

import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11

def __init__():
    pass

def define_pin():
    pin = int(input("Type pin for the data port here :"))
    return pin

def get_data(sensor, pin):
    times = 0
    while times < 10:
        data = hum, temp = Adafruit_DHT.read_retry(sensor, pin)
        print(data)
        times += 1
        time.sleep(1)
    return 1
dhtpin = define_pin()
done = get_data(sensor, dhtpin)
print("Finished 10 measurements.")

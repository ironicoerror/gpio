#! /usr/bin/env python3

import Adafruit_DHT
import time
from datetime import datetime
import argparse

sensor = Adafruit_DHT.DHT11

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("timeinterval", type=int,\
            help="time between two measurements in sec, default=600")
    parser.add_argument("pin", type=int,\
            help="raspi pin connected to the DHT11 data pin, default=17")
    args = parser.parse_args()
    ARG_TIME = int(args.timeinterval)
    ARG_PIN = int(args.pin)
    return ARG_TIME, ARG_PIN

def get_data(sensor, pin):
    humset = []
    tempset = []
    clocktime = str(datetime.now().time())[0:8]
    date = str(datetime.now().date())
    for _ in range(10):
        hum, temp = Adafruit_DHT.read_retry(sensor, pin) 
        humset.append(hum)
        tempset.append(temp)
    avghum = round(sum(humset) / len(humset),1)
    avgtemp = round(sum(tempset) / len(tempset),1)
    data_script = [date, clocktime, avghum, avgtemp]
    return data_script

# program
TIME_TO_NEXT, PIN = parse_arguments()
while True:
    newdata = get_data(sensor,PIN)
    print(newdata[0], ",", newdata[1], ",", newdata[2], ",", newdata[3])
    time.sleep(TIME_TO_NEXT)

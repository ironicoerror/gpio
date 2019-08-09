#! /usr/bin/env python3

import Adafruit_DHT
import time
from datetime import datetime
import argparse
import sys

global sensor

sensor = Adafruit_DHT.DHT11

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("timeinterval", type=int, help='an integer for the time to next meassurement in sec')
    parser.add_argument("pin", type=int,\
            help='an integer for the INPUT PIN on the your board that is connected to the datapin of the DHT11')
    args = parser.parse_args()
    ARG_TIME = int(args.timeinterval)
    ARG_PIN = int(args.pin)
    return ARG_TIME, ARG_PIN

def get_data(sensor, pin):
    times = 0
    humset = []
    tempset = []
    clocktime = str(datetime.now().time())[0:8]
    date = str(datetime.now().date())
    for _ in range(times):
        humset.append(Adafruit_DHT.read_retry(sensor, pin)[0])
        tempset.append(Adafruit_DHT.read_retry(sensor, pin)[1])
        #humset.append(hum)
        #tempset.append(temp)
        times +=1
    avghum = sum(humset) / len(humset)
    avgtemp = sum(tempset) / len(tempset)
    data_script = [date, clocktime, avghum, avgtemp]
    return data_script

# program
TIME_TO_NEXT, PIN = parse_arguments()
while True:
    newdata = get_data(sensor,PIN)
    print(newdata[0], ",", newdata[1], ",", newdata[2], ",", newdata[3])
    time.sleep(TIME_TO_NEXT)

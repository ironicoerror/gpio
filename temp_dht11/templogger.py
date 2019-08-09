#! /usr/bin/env python3

import Adafruit_DHT
import time
from datetime import datetime

global sensor

sensor = Adafruit_DHT.DHT11
def __init__():
    pass

def get_data(sensor, pin):
    times = 0
    sumhum = 0
    sumtemp = 0
    humset = []
    tempset = []
    clocktime = str(datetime.now().time())[0:8]
    date = str(datetime.now().date())

    while times < 10:
        hum, temp = Adafruit_DHT.read_retry(sensor, pin)
        humset.append(hum)
        tempset.append(temp)
        sumhum += humset[times]
        sumtemp += tempset[times]
        times += 1
        time.sleep(1)
    avghum = sumhum / len(humset)
    avgtemp = sumtemp / len(tempset)
    avgdata = [date, clocktime, avghum, avgtemp]
    return avgdata

while True:
    print(10 * "-")
    newdata = get_data(sensor,17)
    print(newdata[0], newdata[1], newdata[2], newdata[3])
    time.sleep(600)


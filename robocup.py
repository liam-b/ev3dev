#!/usr/bin/env python

import ev3dev.ev3 as ev3
import datetime as datetime
import time

rightMotor = ev3.LargeMotor('outA')
colorRight = ev3.ColorSensor('in1')

build = 'alpha 0.3'
running = True
localTime = str(datetime.now())
logFile = open('output.log', 'w')

def log(text):
    logFile.write(text + '\n')

def runRight(speed):
    rightMotor.run_forever(duty_cycle_sp = speed)

def stopRight():
    rightMotor.stop()
    
def sleep(delay):
    time.sleep(delay / 1000)


def start():
    log(localTime + ' | ' + build + '\n')

def loop():
    runRight(50)
    sleep(1000)
    runRight(20)
    sleep(1000)

start()

while running:
    loop()
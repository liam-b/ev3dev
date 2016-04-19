#!/usr/bin/env python

import ev3dev.ev3 as ev3
import time

rightMotor = ev3.LargeMotor('outA')

build = 'alpha 0.1'
running = True
localTime = time.asctime(time.localtime(time.time()))
logFile = open('output.log', 'w')

def log(text):
    logFile.write(text + '\n')

def runRight(speed):
    rightMotor.run_forever(duty_cycle_sp = speed)

def stopRight():
    rightMotor.stop()


def start():
    log(localTime)
    log('running build: ' + build)
    log('starting script')

def loop():
    runRight(50)

start()

while running:
    loop()
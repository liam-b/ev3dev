#!/usr/bin/env python

import ev3dev.ev3 as ev3
import datetime as datetime
import time

class Motor():
    def __init__(self, port):
        self.port = port
        self.motor = ev3.LargeMotor(port)
    
    def run(self, speed):
        self.motor.run_forever(duty_cycle_sp = speed)
    
    def stop(self):
        self.motor.stop()
        
class ColorSensor():
    def __init__(self, sensor, port):
        self.port = port
        self.sensor = ev3.ColorSensor(sensor, port)
        
motorRight = Motor('outA')
colorRight = ColorSensor('ColorSensor', 'in1')

build = 'alpha 0.7'
running = True
localTime = time.strftime('%c')
logFile = open('output.log', 'w')
count = int(0)

def log(text):
    logFile.write(text + '\n')
    print text
    
def sleep(delay):
    time.sleep(delay / 1000)

#####

def start():
    log(localTime + ' | ' + build + '\n')
    log(str(colorRight))
    log(str(colorRight.__dict__.keys()))
    log(str(colorRight.__module__))
    log(str(colorRight.__init__))
    log(str(dir(colorRight)))
    log(str(vars(colorRight)))

def loop():
    motorRight.run(10)
    count = count + 1
    if count > 100:
        running = False

start()

while running:
    loop()
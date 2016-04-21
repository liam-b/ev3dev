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
    def __init__(self, port):
        self.port = port
        self.sensor = ev3.ColorSensor(port)
        
motorRight = Motor('outA')
colorRight = ColorSensor('in1')

build = 'alpha 0.3'
running = True
localTime = time.strftime('%c')
logFile = open('output.log', 'w')

def log(text):
    logFile.write(text + '\n')
    
def sleep(delay):
    time.sleep(delay / 1000)

#####

def start():
    log(localTime + ' | ' + build + '\n')

def loop():
    motorRight.run(50)

start()

while running:
    loop()
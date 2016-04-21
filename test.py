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
        
motorRight = Motor('outA')

# rightMotor = ev3.LargeMotor('outA')
# colorRight = ev3.ColorSensor('in1')

running = True

def sleep(delay):
    time.sleep(delay / 1000)

def loop():
    motorRight.run(50)

while running:
    loop()
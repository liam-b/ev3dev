#!/usr/bin/env python

import ev3dev.ev3 as ev3
import time

class Motor():
    def __init__(self, port):
        self.port = port[2:3]
        self.motor = ev3.LargeMotor(port)
    
    def run(self, speed):
        self.motor.run_forever(duty_cycle_sp = speed)
    
    def stop(self):
        self.motor.stop()
        
class ColorSensor():
    def __init__(self, port):
        self.port = port[2:3]
        self.sensor = ev3.ColorSensor(port)
        
    def value(self):
        return self.sensor.value('0')
    
    def mode(self, mode):
        self.sensor.mode = mode
        
class UltrasonicSensor():
        def __init__(self, port):
            self.port = port[2:3]
            self.motor = ev3.UltrasonicSensor(port)
        
        def value(self):
            return self.sensor.value('0')
            
motorRight = Motor('outA')
# motorLeft = Motor('outB')
colorRight = ColorSensor('in1')

build = 'alpha 1.2'
running = True
localTime = time.strftime('%c')
logFile = open('output.log', 'w')
speed = 0

def log(text):
    logFile.write(text + '\n')
    print text
    
def sleep(delay):
    time.sleep(delay / 1000)

#####

log(localTime + ' | ' + build + '\n')

while running:
    motorRight.run(speed)
    print colorRight.value()
    print colorRight.port

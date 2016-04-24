#!/usr/bin/env python

import ev3dev.ev3 as ev3
import time
import os

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
        
    def value(self, value):
        return self.sensor.value(value)
    
    def mode(self, mode):
        self.sensor.mode = mode
        
class UltrasonicSensor():
        def __init__(self, port):
            self.port = port[2:3]
            self.sensor = ev3.UltrasonicSensor(port)
        
        def value(self):
            return self.sensor.value('0')
            
motorRight = Motor('outA')
# motorLeft = Motor('outB')

colorRight = ColorSensor('in1')

build = 'alpha 1.4'
running = True
localTime = time.strftime('%c')
logFile = open('output.log', 'w')
speed = 0

def log(text):
    logFile.write(text + '\n')
    print text
    
def sleep(delay):
    time.sleep(delay / 1000)
    
def starwars():
    ev3.Sound.tone([(392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
    (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
    (392, 700, 100)]).wait()

#####

# starwars()
log(localTime + ' | ' + build + '\n')
colorRight.mode('RGB-RAW')

while running:
    motorRight.run(speed)
    print str(colorRight.value(0)) + ' | ' + str(colorRight.value(1)) + ' | ' + str(colorRight.value(2)) + ' | ' + str((colorRight.value(0) + colorRight.value(1) + colorRight.value(2)) / 3)

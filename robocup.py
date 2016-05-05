#!/usr/bin/env python

import ev3dev.ev3 as ev3
from motor import *
from sensor import *
import sound
import starwars
import time
            
motorRight = Motor('outA')
motorLeft = Motor('outB')
# motorLeft = Motor('outC')

colorRight = ColorSensor('in1')
colorLeft = ColorSensor('in2')

# ultrasonic = UltrasonicSensor('in2')

build = 'alpha 1.6'
running = True
localTime = time.strftime('%c')
    
def sleep(delay):
    time.sleep(delay / 1000)
    
def run(right, left):
    motorRight.run(right)
    motorLeft.run(left)

def stop():
    motorRight.stop()
    motorLeft.stop()

#####

# starwars.play()
print localTime + ' | ' + build
# colorRight.mode('RGB-RAW')

while running:
    # print colorRight.rgbValue()
    # print ultrasonic.value(0)
    
    command = raw_input()
    
    if command == 'w':
        run(75, 75)
    elif command == 's':
        run(-75, -75)
    elif command == 'd':
        run(-75, 75)
    elif command == 'a':
        run(75, -75)
    elif command == 'e':
        run(40, 75)
    elif command == 'q':
        run(75, 40)
    elif command == '':
        stop()
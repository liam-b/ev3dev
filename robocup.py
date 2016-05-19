#!/usr/bin/env python

import ev3dev.ev3 as ev3
from py/motor import *
from py/sensor import *
import py/sound
import tone/starwars
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
colorRight.mode('COL-REFLECT')
BLACK = 30

#####

def followLine():
    if colorRight.value(0) < 20:
        run(-40, 60)
    # elif colorRight.value(0) < 50:
    #     run(40, 60)
    elif colorLeft.value(0) < 20:
        run(60, -40)
    # elif colorLeft.value(0) < 50:
    #     run(60, 40)
    else:
        run(40, 40)
    
def control():
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

while running:
    followLine()
    print str(colorRight.value(0)) + ' | ' + str(colorLeft.value(0))
    # print ultrasonic.value(0)
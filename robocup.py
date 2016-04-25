#!/usr/bin/env python

import ev3dev.ev3 as ev3
from modules import *
import starwars
import time
            
motorRight = Motor('outA')
# motorLeft = Motor('outB')
# motorLeft = Motor('outC')

colorRight = ColorSensor('in1')
# colorLeft = ColorSensor('in1')

ultrasonic = UltrasonicSensor('in4')

build = 'alpha 1.4'
running = True



# starwars.play()
print localTime + ' | ' + build
colorRight.mode('COL-COLOR')
    # rgb = RGB-RAW
    # reflect = COL-REFLECT
    # color = COL-COLOR

def followLine():
    if colorRight.value(0) > 4: 
        ev3.Sound.beep()
        while colorRight.value(0) > 4:
            sleep(1)

while running:
    # if foundGreen():
    #     turnOnGreen()
    #     
    # if foundWaterTower():
    #     evadeWaterTower()
    #     
    # if foundSpill():
    #     enterSpill()
    
    # followLine()
    print '[' + str(colorRight.value(0)) + ', ' + str(ultrasonic.value(0)) + ']'
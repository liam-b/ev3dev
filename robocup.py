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

ultrasonic = UltrasonicSensor('in2')

build = 'alpha 1.4'
running = True
localTime = time.strftime('%c')


# starwars.play()
print localTime + ' | ' + build
colorRight.mode('RGB-RAW')

while running:
    print colorRight.rgbValue()

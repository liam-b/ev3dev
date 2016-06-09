#!/usr/bin/env python

import ev3dev.ev3 as ev3
from motor import *
from sensor import *
import time
from logger import Logger

output = Logger('log/output.log')
            
motorRight = Motor('outA')
motorLeft = Motor('outB')
motorClaw = Motor('outC')

colorRight = ColorSensor('in1')
colorLeft = ColorSensor('in4')
ultrasonic = UltrasonicSensor('in2')
# gyro = GyroSensor('in3')

build = 'beta 1.1'
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
    
def mode(newMode):
    colorRight.mode(newMode)
    colorLeft.mode(newMode)
    
def setupClaw():
    motorClaw.run(-10)
    sleep(2000)
    motorClaw.run(10)
    sleep(3000)
    motorClaw.stop()
        
def positionState():
    if colorRight.value(0) < 20 and colorLeft.value(0) < 20:
        return 'doubleBlack'
    elif colorRight.value(0) < 3 and colorLeft.value(0) < 3:
        return 'fullBlack'
    elif  colorRight.value(0) > 20 and colorLeft.value(0) > 20:
        return 'doubleWhite'
    elif colorRight.value(0) > 20 and colorLeft.value(0) < 20 or colorRight.value(0) < 20 and colorLeft.value(0) > 20:
        return 'whiteBlack'
    else:
        return 'unknown'

#####

output.log('started robot, running version ' + build)
output.log('setting color sensor modes')
mode('COL-REFLECT')
output.log('calibrating claw')
setupClaw()
output.log('starting course at: ' + positionState())
output.log('-------')
output.log('following line')

followCount = 0

#####

def followLine():        
    global followCount
    
    if colorRight.value(0) < 25:
        run(-80, 75)
    elif colorRight.value(0) < 50:
        run(40, 75)
    elif colorLeft.value(0) < 20:
        run(75, -80)
    elif colorLeft.value(0) < 50:
        run(75, 40)
    else:
        run(75, 75)
    
    followCount += 1
    
    if followCount > 100:
        followCount = 0;
        output.log('following line')
        
def turnGreen():
    mode('COL-COLOR')
    output.log('black colors are ' + str(colorRight.value(0)) + ' | ' + str(colorLeft.value(0)))
    if colorLeft.value(0) == 3:
        output.log('turning left')
        turn(motorLeft)
    elif colorRight.value(0) == 3:
        output.log('turning right')
        turn(motorRight)
    elif colorLeft.value(0) == 3 and colorRight.value(0) == 3:
        output.warn('both sensors on green, trying again')
        run(-50, -50)
        sleep(1000)
        run(50, 50)
        sleep(1000)
    elif colorLeft.value(0) == 1 and colorRight.value(0) == 1:
        output.log('going forward')
        run(50, 50)
        sleep(1000)
    else:
        output.warn('bad values, trying again')
        run(-50, -50)
        sleep(1000)
        run(50, 50)
        sleep(1000)
        
    mode('COL-REFLECT')
        
def turn(motor):
    run(50, 50)
    sleep(1000)
    motor.run(-50)
    sleep(1000)

while running:
    followLine()
    
    if positionState() == 'doubleBlack':
        output.log('spotted double black at: ' + str(colorRight.value(0)) + ' | ' + str(colorLeft.value(0)))
        stop()
        turnGreen()
        output.log('finished green at: ' + str(colorRight.value(0)) + ' | ' + str(colorLeft.value(0)))
        output.log('following line')
        
    if ultrasonic.value(0) > 505:
        output.log('found water tower at: ' + str(ultrasonic.value(0)))
        run(60, -60)
        sleep(1000)
        run(35, 75)
        while colorLeft.value(0) > 20:
            pass
        sleep(100)
        run(60, -50)
        sleep(1000)
        output.log('avoided water tower')
        output.log('following line')
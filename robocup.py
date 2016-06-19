#!/usr/bin/env python

import ev3dev.ev3 as ev3
from lib.motor import *
from lib.sensor import *
from lib.logger import *
from lib.sound import *
import time

sound = Sound()
output = Logger('log/output.log')
            
motorRight = Motor('outA')
motorLeft = Motor('outB')
motorClaw = Motor('outC')

colorRight = ColorSensor('in1')
colorLeft = ColorSensor('in4')
ultrasonic = UltrasonicSensor('in2')
gyro = GyroSensor('in3')

build = 'beta 1.1'
running = True

#####

followCount = 0
doLineFollow = True
doGreenTurn = True
doAvoidWaterTower = True

WHITE = 70
BLACK = 25
AVERAGE = (WHITE + BLACK) / 2

FORWARD_SPEED = 70
SPEED_SLOW = 40
BACKWARDS_SPEED = 40
TURN_SPEED = -80
TURN_FORWARD_SPEED = 80
AVOID_SPEED = 40

TURN_THRESHOLD = 27
AVOID_THRESHOLD = 50
ULTRASONIC_THRESHOLD = 180

GREEN_TURN_SPEED = 0
GREEN_TURN_DELAY = 0
GREEN_FORWARD_DELAY = 0

#####

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
    time.sleep(2)
    motorClaw.run(10)
    time.sleep(3)
    motorClaw.stop()
        
def positionState():
    if colorRight.value(0) < BLACK and colorLeft.value(0) < BLACK:
        return 'doubleBlack'
    elif colorRight.value(0) < 3 and colorLeft.value(0) < 3:
        return 'fullBlack'
    elif  colorRight.value(0) > 20 and colorLeft.value(0) > 20:
        return 'doubleWhite'
    elif colorRight.value(0) > 20 and colorLeft.value(0) < 20 or colorRight.value(0) < 20 and colorLeft.value(0) > 20:
        return 'whiteBlack'
    else:
        return 'unknown'

def followLine():        
    if colorRight.value(0) < TURN_THRESHOLD:
        run(TURN_SPEED, TURN_FORWARD_SPEED)
    elif colorRight.value(0) < AVOID_THRESHOLD:
        run(AVOID_SPEED, FORWARD_SPEED)
    elif colorLeft.value(0) < TURN_THRESHOLD:
        run(TURN_FORWARD_SPEED, TURN_SPEED)
    elif colorLeft.value(0) < AVOID_THRESHOLD:
        run(FORWARD_SPEED, AVOID_SPEED)
    else:
        run(FORWARD_SPEED, FORWARD_SPEED)
        
def turnGreen():
    mode('COL-COLOR')
    run(SPEED_SLOW, SPEED_SLOW)
    time.sleep(0.3)
    output.log('black colors are ' + str(colorRight.value(0)) + ' | ' + str(colorLeft.value(0)))
    if colorLeft.value(0) == 3:
        output.log('turning left')
        greenTurn(motorLeft, colorRight)
    elif colorRight.value(0) == 3:
        output.log('turning right')
        greenTurn(motorRight, colorLeft)
    elif colorLeft.value(0) == 3 and colorRight.value(0) == 3:
        output.warn('both sensors on green, trying again')
        greenTryAgain()
    elif colorLeft.value(0) == 1 and colorRight.value(0) == 1:
        output.log('going forward')
        run(50, 50)
        time.sleep(1)
    else:
        output.warn('bad values, trying again')
        greenTryAgain()
        
    mode('COL-REFLECT')
        
def greenTurn(motor, sensor):
    run(50, 50)
    time.sleep(0.6)
    motor.run(-50)
    while sensor.value(0) != 1:
        pass
    
def greenTryAgain():
    run(-50, -50)
    time.sleep(0.3)
    run(50, 50)
    time.sleep(0.3)
    
def checkForGreen():
    if positionState() == 'doubleBlack':
        output.log('spotted double black at: ' + str(colorRight.value(0)) + ' | ' + str(colorLeft.value(0)))
        stop()
        turnGreen()
        output.log('finished green at: ' + str(colorRight.value(0)) + ' | ' + str(colorLeft.value(0)))
        output.log('following line')

def checkForWaterTower():        
    if ultrasonic.value(0) < ULTRASONIC_THRESHOLD:
        run(-SPEED_SLOW, -SPEED_SLOW)
        time.sleep(0.8)
        output.log('found water tower at: ' + str(ultrasonic.value(0)))
        run(60, -60)
        time.sleep(1)
        run(25, 75)
        while colorLeft.value(0) > 30:
            pass
        time.sleep(0.1)
        run(60, -50)
        time.sleep(1)
        output.log('avoided water tower')
        output.log('following line')
        
def checkForSpill():
    if colorRight.value(0) > 83 and colorLeft.value(0) > 83:
        run(SPEED_SLOW, SPEED_SLOW)
        time.sleep(0.3)
        mode('COL-COLOR')
        if colorLeft.value(0) == 3 and colorRight.value(0) == 3:
            sound.beep()
            stop()
            findCan()
            
def findCan():
    run(SPEED_SLOW, SPEED_SLOW)
    time.sleep(3)
    stop()
    time.sleep(100)
    
output.log('started robot, running version ' + build)
output.log('setting color sensor modes')
mode('COL-REFLECT')
output.log('calibrating claw')
# setupClaw()
output.log('starting course at: ' + positionState())
output.log('-------')
output.log('following line')

while running:
    followLine()
    checkForGreen()
    # checkForWaterTower()
    checkForSpill()
    print str(colorLeft.value(0)) + ' | ' + str(colorLeft.value(0))
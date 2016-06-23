#!/usr/bin/env python

import ev3dev.ev3 as ev3
from lib.all import *
from bot import *
import time

sound = Sound()
output = Logger('log/output.log')

motorRight = Motor(outA)
motorLeft = Motor(outB)
motorClaw = Motor(outC)

colorRight = ColorSensor(in1)
colorLeft = ColorSensor(in4)
ultrasonic = UltrasonicSensor(in2)
gyro = GyroSensor(in3)

output.log('started robot, running version ' + build)
output.log('setting color sensor modes')
mode('COL-REFLECT')
if bot.calibrateClaw:
    output.log('calibrating claw')
    setupClaw()
output.log('starting course at: ' + bot.state())
output.log('-------')
output.log('following line')

while running:
    if bot.doLineFollow: bot.followLine()
    if bot.doGreenCheck: bot.checkForGreen()
    if bot.avoidWaterTower: bot.checkForWaterTower()
    if bot.searchForSpill: bot.checkForSpill()
    # print str(colorLeft.value(0)) + ' | ' + str(colorLeft.value(0))

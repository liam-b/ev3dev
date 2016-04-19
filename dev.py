#!
import ev3dev.ev3 as ev3
import time

rightMotor = ev3.LargeMotor('outA')

def runRight(speed):
    rightMotor.run_forever(duty_cycle_sp = speed)
    
def stopRight():
    rightMotor.stop()

runRight(100)
time.sleep(3)
stopRight()
time.sleep(3)
#!
import ev3dev.ev3 as ev3
import time

rightMotor = ev3.LargeMotor('outA')

build = 'alpha 0.1'
running = True
localTime = time.asctime(time.localtime(time.time()))

logFile = open('log.txt', 'w')
def log(text, status):
    logFile.write('[' + status + '] ' + text + '\n')
    
log('logging: ' + localTime,'OUT')
log('running build: ' + build,'OUT')

def runRight(speed):
    rightMotor.run_forever(duty_cycle_sp = speed)
    
def stopRight():
    rightMotor.stop()

# runRight(100)
# time.sleep(3)
# stopRight()
time.sleep(3)
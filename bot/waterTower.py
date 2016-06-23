from constants import *

def checkForWaterTower():
    global avoidWaterTower
    if ultrasonic.value(0) < ULTRASONIC_THRESHOLD and avoidNextWaterTower:
        if skipSecondWaterTower:
            avoidNextWaterTower = False
        avoidWaterTower()

def avoidWaterTower():
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

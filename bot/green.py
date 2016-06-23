from constants import *

def checkForGreen():
    if state() == 'doubleBlack':
        output.log('spotted double black at: ' + str(colorRight.value(0)) + ' | ' + str(colorLeft.value(0)))
        stop()
        turnGreen()
        output.log('finished green at: ' + str(colorRight.value(0)) + ' | ' + str(colorLeft.value(0)))
        output.log('following line')

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

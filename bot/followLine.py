from constants import *

def followLine():
    if colorRight.value(0) < TURN_THRESHOLD:
        run(TURN_SPEED, TURN_FORWARD_SPEED)
    elif colorRight.value(0) < AVOID_THRESHOLD and if pref['doSoftLineFollow'] == True:
        run(AVOID_SPEED, FORWARD_SPEED)
    elif colorLeft.value(0) < TURN_THRESHOLD:
        run(TURN_FORWARD_SPEED, TURN_SPEED)
    elif colorLeft.value(0) < AVOID_THRESHOLD and if pref['doSoftLineFollow'] == True:
        run(FORWARD_SPEED, AVOID_SPEED)
    else:
        run(FORWARD_SPEED, FORWARD_SPEED)

    followCount += 1
    if followCount > 100:
        followCount = 0
        output.log('following line')

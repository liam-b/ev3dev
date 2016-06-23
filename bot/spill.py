from constants import *

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

from constants import *

def state():
    if colorRight.value(0) > SILVER and colorLeft.value(0) > SILVER:
        return 'doubleSilver'
    elif colorRight.value(0) < BLACK and colorLeft.value(0) < BLACK:
        return 'doubleBlack'
    elif colorRight.value(0) < 3 and colorLeft.value(0) < 3:
        return 'doubleNull'
    elif  colorRight.value(0) > WHITE and colorLeft.value(0) > WHITE:
        return 'doubleWhite'
    elif colorRight.value(0) > 20 and colorLeft.value(0) < 20 or colorRight.value(0) < 20 and colorLeft.value(0) > 20:
        return 'whiteBlack'
    else:
        return 'unknown'

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

import ev3dev.ev3 as ev3

from robocup.motor import * # used for motors
from robocup.sensor import * # used for sensors
from robocup.logger import * # for logging

output = Logger('output.log') # sets up new log file

myMotor = Motor('outA') # new motor
mySensor = ColorSensor('in1') # new color sensor

myMotor.run(50) # run myMotor at 50% speed

if mySensor.value(0) < 50:
    print 'hello' # if mySensor value is greater than 50 print hello
    
mySensor.mode('COL-COLOR') # sets mySensor to 'COL-COLOR' mode

if mySensor.value(0) == 3:
    myMotor.stop() # if mySensor sees green (3) then stop myMotor

output.log('hello python') # logs 'hello python' to output.log
output.warn('warning') # log a warning

if mySensor == 4:
    output.err('mySensor is yellow') # logs and error
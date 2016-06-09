# Robocup using ev3dev

This is a [robocup](http://www.robocupjunior.org.au/) program running [ev3dev](https://http://www.ev3dev.org/) with python. I have put together a library to make it a little easier to work with but it mainly the same as what the guys over at ev3dev built. You can go over to http://www.ev3dev.org/ to learn how to install ev3dev onto your EV3. Once you have that installed and running (which may take a while and a few tries) you will need to download my library. Just as a note you will definitely need to know a good amount of python to use this library.

# Docs for the library

Once the library is all installed you will need to import it into your python file using:

```python
from robocup.motor import *
from robocup.sensor import *
```

This grabs all the motor and sensor classes. You'll also need to import ev3dev with:

```python
import ev3dev.ev3 as ev3
```

Thats pretty much it for the imports, onto how to use the classes.

### Motors

To setup a new motor you need to make it a new motor class and give it a port like:

```python
newMotor = Motor('outA') # You can go from ports 'outA' through to 'outD'
```

Once you have a motor setup you can preform the following commands:

```python
newMotor.run(80) # speed to run at (runs forever until stop())
newMotor.stop() # stops motor
newMotor.position() # returns the motors current rotation
newMotor.reset() # resets rotation to 0
```

### Sensors

Like a motor to set up a sensor write:

```python
colorSensor = ColorSensor('in1') # You can go from ports 'in1' through to 'in4'
ultrasonicSensor = UltrasonicSensor('in2')
gyroSensor = GyroSensor('in3') # Other sensors are coming
```

Once you have a motor setup you can preform the following commands:

##### Color Sensor
```python
colorSensor.value(0) # this is the main value for most modes though it can range up to value(2)
colorSensor.mode('COL-REFLECT') # changes the sensors mode list of modes are: 
# 'COL-REFLECT' reflected light value [value(0)] 0 - 100
# 'COL-AMBIENT' ambient light value [value(0)] 0 - 100
# 'COL-COLOR' predefined color value [value(0)] 0 - 7
# 'REF-RAW' no idea [value(0)] 0 - 1020
# 'RGB-RAW' raw rgb values (use sensor.rgb() for array format) [value(0), value(1), value(3)] 0 - 1020
# 'COL-CAL' no idea
colorSensor.rgb() # returns array of value(0) to value(2)
```

##### Ultrasonic Sensor
```python
ultrasonicSensor.value(0) # this is the only value ranging from 0 - 2550
```

##### Gyro Sensor
```python
gyroSensor.value(0) # this is the only value ranging from 0 - 2550
gyroSensor.mode('GYRO-ANG') # changes the sensors mode list of modes are: 
# 'GYRO-ANG' angle [value(0)] -32768 - 32767
# 'GYRO-RATE' turning speed rate [value(0)] -440 to 440
```

### Logger

If you want to use my logger as well import with:

```python
from robocup.logger import *
```

To log to a new file and write to it use:

```python
output = Logger('log/output.log') # path for new log

output.log('hello')
output.warn('warning') # logs warning
output.err('warning') # logs error
```

For this you might want to install a .log file grammer (for atom) such as https://atom.io/packages/language-log

# Robocup using ev3dev

This is a [robocup](http://www.robocupjunior.org.au/) program running [ev3dev](https://http://www.ev3dev.org/) with python. I have put together a library to make it a little easier to work with but it mainly the same as what the guys over at ev3dev built. You can go over to http://www.ev3dev.org/ to learn how to install ev3dev onto your EV3. Once you have that installed and running (which may take a while and a few tries) you will need to download my library.

# Docs

Once the library is all installed you will need to import it into your python file using:

```python
from motor import *
from sensor import *
```

This grabs all the motor and sensor classes. You'll also need to import ev3dev with:

```python
import ev3dev.ev3 as ev3
```

Thats pretty much it for the imports, onto how to use the classes.

## Motors

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

import ev3dev.ev3 as ev3

class Motor():
    def __init__(self, port):
        self.port = port[2:3]
        self.motor = ev3.LargeMotor(port)
    
    def run(self, speed):
        self.motor.run_forever(duty_cycle_sp = speed)
    
    def stop(self):
        self.motor.stop()
        
class ColorSensor():
    def __init__(self, port):
        self.port = port[2:3]
        self.sensor = ev3.ColorSensor(port)
        
    def value(self, value):
        return self.sensor.value(value)
    
    def mode(self, mode):
        self.sensor.mode = mode
        
    def rgb(self):
        return [self.sensor.value(0), self.sensor.value(1), self.sensor.value(2)]
        
    def rgbValue(self):
        return (self.sensor.value(0) + self.sensor.value(1) + self.sensor.value(2)) / 3
        
class UltrasonicSensor():
        def __init__(self, port):
            self.port = port[2:3]
            self.sensor = ev3.UltrasonicSensor(port)
        
        def value(self, value):
                return int((2550 - self.sensor.value(value)) / 5)

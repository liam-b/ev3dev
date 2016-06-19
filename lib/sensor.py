import ev3dev.ev3 as ev3

class ColorSensor():
    def __init__(self, port):
        self.port = port[2:3]
        self.sensor = ev3.ColorSensor(port)
        self.sensor.mode = 'COL-COLOR'
        
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
            return self.sensor.value(value)
                
class GyroSensor():
    def __init__(self, port):
        self.port = port[2:3]
        self.sensor = ev3.GyroSensor(port)
    
    def value(self, value):
        return self.sensor.value(value)
        
    def mode(self, mode):
        self.sensor.mode = mode
        
class TouchSensor():
    def __init__(self, port):
        self.port = port[2:3]
        self.sensor = ev3.TouchSensor(port)
    
    def value(self, value):
        return self.sensor.value(value)
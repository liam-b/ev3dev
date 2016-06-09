import ev3dev.ev3 as ev3

class Motor():
    def __init__(self, port):
        self.port = port[2:3]
        self.motor = ev3.LargeMotor(port)
    
    def run(self, speed):
        self.motor.run_forever(duty_cycle_sp = speed)
    
    def stop(self):
        self.motor.stop()
        
    def reset(self):
        self.motor.reset()
    
    def position(self):
        return self.motor.position
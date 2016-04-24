from ev3dev.ev3 import Msensor
d = Msensor(port=1)
print (d.type_id) #read type_id file 
print (d.value1) #read value1 file
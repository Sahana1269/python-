#program to run a motor and sensor
import RPi.GPIO as gp
from time import sleep


gp.setmode(gp.BCM)
gp.setup(16,gp.IN)
MotorA=9
MotorB=25
drive=True
gp.setup(MotorA,gp.OUT)
gp.setup(MotorB,gp.OUT)
gp.output(MotorA,gp.HIGH)
gp.output(MotorB,gp.LOW)

while True:
    
   
    if gp.input(16):
        gp.output(MotorA,gp.HIGH)
        print("Have a safe journey!")
        
    else:
         
        print("Not allowed to drive")
        gp.output(MotorA,gp.LOW)
    sleep(1)

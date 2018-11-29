import RPi.GPIO as GPIO
import time,sys
from time import sleep

MotorA=9
MotorB=25
drive=True

GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(MotorA,GPIO.OUT)
GPIO.setup(MotorB,GPIO.OUT)
GPIO.output(MotorA,GPIO.HIGH)
GPIO.output(MotorB,GPIO.LOW)

        

def action(pin):
    print("sensor detected!")
    drive = False    

GPIO.add_event_detect(16,GPIO.RISING)
GPIO.add_event_callback(16,action)


try:
    while True:
        if not(drive):
            print("not safe")
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()

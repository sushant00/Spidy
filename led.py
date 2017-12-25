import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16


GPIO.setup(Motor1A,GPIO.OUT)
GPIO.output(Motor1A,GPIO.HIGH)

sleep(5)
GPIO.output(Motor1A,GPIO.LOW)
 
GPIO.cleanup()

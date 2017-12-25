from time import sleep
import webiopi
GPIO = webiopi.GPIO

#help esc run bldc
import pigpio
#import RPi.GPIO as BLDCGPIO

#DC motor pins 
Motor1A = 23
Motor1B = 24
Motor1E = 25

Motor2A = 11
Motor2B = 9
Motor2E = 10
 
Motor3A = 6
Motor3B = 19
Motor3E = 26

Motor4A = 16
Motor4B = 20
Motor4E = 21

#ESC pin i.e. used to control BLDC
GPIO_ESC = 13

def setup():
	#setup for DC motor pins
	GPIO.setFunction(Motor1A,GPIO.OUT)
	GPIO.setFunction(Motor1B,GPIO.OUT)
	GPIO.setFunction(Motor1E,GPIO.OUT)

	GPIO.setFunction(Motor2A,GPIO.OUT)
	GPIO.setFunction(Motor2B,GPIO.OUT)
	GPIO.setFunction(Motor2E,GPIO.OUT)
	 
	GPIO.setFunction(Motor3A,GPIO.OUT)
	GPIO.setFunction(Motor3B,GPIO.OUT)
	GPIO.setFunction(Motor3E,GPIO.OUT)

	GPIO.setFunction(Motor4A,GPIO.OUT)
	GPIO.setFunction(Motor4B,GPIO.OUT)
	GPIO.setFunction(Motor4E,GPIO.OUT)



	#setup for ESC control pin
	#BLDCGPIO.setmode(BLDCGPIO.BCM)
	pigpio = pigpio.pi()

	# ESC calibaration: set max speed then min speed
	pigpio.set_servo_pulsewidth(GPIO_ESC, 2000)
	sleep(2)
	pigpio.set_servo_pulsewidth(GPIO_ESC, 1000)
	sleep(2)

#	DC motor functions used for locomotion
def forward():
	GPIO.digitalWrite(Motor1A,GPIO.HIGH)
	GPIO.digitalWrite(Motor1B,GPIO.LOW)
	GPIO.digitalWrite(Motor1E,GPIO.HIGH)

	GPIO.digitalWrite(Motor2A,GPIO.HIGH)
	GPIO.digitalWrite(Motor2B,GPIO.LOW)
	GPIO.digitalWrite(Motor2E,GPIO.HIGH)
	
	GPIO.digitalWrite(Motor3A,GPIO.LOW)
	GPIO.digitalWrite(Motor3B,GPIO.HIGH)
	GPIO.digitalWrite(Motor3E,GPIO.HIGH)
	
	GPIO.digitalWrite(Motor4A,GPIO.LOW)
	GPIO.digitalWrite(Motor4B,GPIO.HIGH)
	GPIO.digitalWrite(Motor4E,GPIO.HIGH)	


def reverse():
	GPIO.digitalWrite(Motor4A,GPIO.HIGH)
	GPIO.digitalWrite(Motor4B,GPIO.LOW)
	GPIO.digitalWrite(Motor4E,GPIO.HIGH)

	GPIO.digitalWrite(Motor3A,GPIO.HIGH)
	GPIO.digitalWrite(Motor3B,GPIO.LOW)
	GPIO.digitalWrite(Motor3E,GPIO.HIGH)
	
	GPIO.digitalWrite(Motor2A,GPIO.LOW)
	GPIO.digitalWrite(Motor2B,GPIO.HIGH)
	GPIO.digitalWrite(Motor2E,GPIO.HIGH)
	
	GPIO.digitalWrite(Motor1A,GPIO.LOW)
	GPIO.digitalWrite(Motor1B,GPIO.HIGH)
	GPIO.digitalWrite(Motor1E,GPIO.HIGH)

def right():
	GPIO.digitalWrite(Motor1A,GPIO.HIGH)
	GPIO.digitalWrite(Motor1B,GPIO.LOW)
	GPIO.digitalWrite(Motor1E,GPIO.HIGH)

	GPIO.digitalWrite(Motor2A,GPIO.HIGH)
	GPIO.digitalWrite(Motor2B,GPIO.LOW)
	GPIO.digitalWrite(Motor2E,GPIO.HIGH)
	
	GPIO.digitalWrite(Motor3E,GPIO.LOW)
	
	GPIO.digitalWrite(Motor4E,GPIO.LOW)  

def left():
	GPIO.digitalWrite(Motor1E,GPIO.LOW)

	GPIO.digitalWrite(Motor2E,GPIO.LOW)
	
	GPIO.digitalWrite(Motor3A,GPIO.LOW)
	GPIO.digitalWrite(Motor3B,GPIO.HIGH)
	GPIO.digitalWrite(Motor3E,GPIO.HIGH)
	
	GPIO.digitalWrite(Motor4A,GPIO.LOW)
	GPIO.digitalWrite(Motor4B,GPIO.HIGH)
	GPIO.digitalWrite(Motor4E,GPIO.HIGH)

def stop():
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)
	GPIO.output(Motor3E,GPIO.LOW)
	GPIO.output(Motor4E,GPIO.LOW)


#BLDC motor functions
def one():
	pigpio.set_servo_pulsewidth(GPIO_ESC,1000)	#min speed

def two():	
	pigpio.set_servo_pulsewidth(GPIO_ESC, 1500)	

def three():
	pigpio.set_servo_pulsewidth(GPIO_ESC, 2000)	#max speed

def stopbldc():
	pigpio.set_servo_pulsewidth(GPIO_ESC, 0)	#stop the pulses


# webiopi commands called by html page
@webiopi.macro
def Forward():
	forward()
	
@webiopi.macro
def Reverse():
	reverse()


@webiopi.macro
def LeftTurn():
	left()

@webiopi.macro
def RightTurn():
	right()

@webiopi.macro
def Stop():
	stop()


# call functions to control ESC
@webiopi.macro
def OneSpeed():
	one()

@webiopi.macro
def TwoSpeed():
	two()

@webiopi.macro
def ThreeSpeed():
	three()

@webiopi.macro
def StopBLDC():
	stopbldc()

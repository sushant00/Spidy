from time import sleep
import webiopi
GPIO = webiopi.GPIO

 
Motor1A = 23
Motor1B = 24
Motor1E = 25

Motor2A = 11
Motor2B = 9
Motor2E = 10
 
Motor3A = 13
Motor3B = 19
Motor3E = 26

Motor4A = 16
Motor4B = 20
Motor4E = 21

def setup():
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

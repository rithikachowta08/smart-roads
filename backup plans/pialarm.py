import RPi.GPIO as GPIO
import time

def beep():
	GPIO.setmode(GPIO.BOARD)       # consider physical location number i.e pin number not GPIO number
	GPIO.setwarnings(False)        # disables warnings
	GPIO.setup(11, GPIO.OUT)       # buzzer 1
	GPIO.setup(13, GPIO.OUT)       # buzzer 2
	GPIO.setup(16,GPIO.OUT)        # led 1
	GPIO.setup(12,GPIO.OUT)        # led 2	
	print "Turning LEDs on"
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(12,GPIO.HIGH)
	GPIO.output(11, GPIO.HIGH)
	GPIO.output(13, GPIO.HIGH)
	print("now buzzing")
	time.sleep(2)                 # buzzer 1 on for 3 secs
	GPIO.output(11, GPIO.LOW)                 # no beep
	GPIO.output(13, GPIO.LOW)
	print "Turning LEDs off"
	GPIO.output(16,GPIO.LOW)
	GPIO.output(12,GPIO.LOW)
	last_beep = time.time()
	GPIO.cleanup()

beep()



import RPi.GPIO as GPIO
import time

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
print("I am buzzer 11")
time.sleep(3)                 # buzzer 1 on for 3 secs
GPIO.output(11, GPIO.LOW)
time.sleep(4)                 # no beep
GPIO.output(13, GPIO.HIGH)
print("I am buzzer 13")
time.sleep(3)                 # buzzer 2 on for 3 secs
GPIO.output(13, GPIO.LOW)
print "Turning LEDs off"
GPIO.output(16,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
GPIO.cleanup()
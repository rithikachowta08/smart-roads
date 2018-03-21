import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.output(23,GPIO.HIGH)
print("23 is on")
GPIO.output(18,GPIO.HIGH)
print("18 is on")
time.sleep(5)
GPIO.output(23,GPIO.LOW)
GPIO.output(18,GPIO.LOW)





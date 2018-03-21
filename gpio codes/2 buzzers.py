
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)
print("I am buzzer 11")
time.sleep(3)
GPIO.output(11, GPIO.LOW)
time.sleep(4)
GPIO.output(13, GPIO.HIGH)
print("I am buzzer 13")
time.sleep(3)
GPIO.output(13, GPIO.LOW)
GPIO.cleanup()

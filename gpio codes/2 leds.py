import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

GPIO.setup(23, GPIO.OUT)

GPIO.output(18, True)
print("i am 18")
time.sleep(3)
GPIO.output(18, False)
time.sleep(1)

'''GPIO.output(23, True)
print("i am 23")
time.sleep(3)
GPIO.output(23, False) '''

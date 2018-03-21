'''27/2/18  Created by   
			Rithika Chowta 
			Priya Shetty
			Sharan Preetha Noronha'''

from cv2 import *
import RPi.GPIO as GPIO
from time import *

# flags indicating if car has been detected in video feed from camera 1 and 2
f1, f2 = False, False
last_beep = 0		   # initializing variable to indicate timing of last_beep


def beep():			   # called when cars detected on both sides
    global last_beep
    if int(time()-last_beep) > 5:      # to ensure gap of atleast 5 seconds between consecutive beeps
        # consider physical location number i.e pin number not GPIO number
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)        # disables warnings
        GPIO.setup(11, GPIO.OUT)       # buzzer 1
        GPIO.setup(13, GPIO.OUT)       # buzzer 2
        GPIO.setup(16, GPIO.OUT)        # led 1
        GPIO.setup(12, GPIO.OUT)        # led 2
        print("Switching LEDs on")
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        print("Switching buzzers on for 3 seconds")
        sleep(3)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        print("Turning LEDs off")
        GPIO.output(16, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        last_beep = time()
        GPIO.cleanup()

 # capture frames from a video
cap1 = VideoCapture(0)
cap2 = VideoCapture(1)
#cap = VideoCapture("video.avi")
# XML file describing some features of cars
car_cascade = CascadeClassifier('cars.xml')

while True:
    ret1, frame1 = cap1.read()   # Reads next frame from video and returns boolean value
    ret2, frame2 = cap2.read()
    gray1 = cvtColor(frame1, COLOR_BGR2GRAY)  # Convert to gray scale
    gray2 = cvtColor(frame2, COLOR_BGR2GRAY)
    cars1 = car_cascade.detectMultiScale(gray1, 1.3, 5)  # Detects cars of different sizes
    cars2 = car_cascade.detectMultiScale(gray2, 1.3, 5)
    print(cars1, cars2)
    for (x, y, w, h) in cars1:   # To draw a rectangle on each car from the current frame
        rectangle(frame1, (x, y), (x+w, y+h), (255, 255, 0), 2)
        f1 = True
    for (a, b, c, d) in cars2:
        rectangle(frame2, (a, b), (a+c, b+d), (0, 255, 0), 2)
        f2 = True
    if f1 and f2:
        print("calling beep")
        beep()
        f1, f2 = False, False	# Resetting flags

    namedWindow('Camera 1', WINDOW_NORMAL)    # Displays frame in a 25x25 window
    resizeWindow('Camera 1', 25, 25)
    imshow('Camera 1', frame1)

    namedWindow('Camera 2', WINDOW_NORMAL)
    resizeWindow('Camera 2', 25, 25)
    imshow('Camera 2', frame2)

    if waitKey(33) == 27:   # Wait for Esc key to stop
        break

destroyAllWindows()   # Closes all windows

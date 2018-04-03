# OpenCV Python program to detect cars in video
# import libraries of python OpenCV 
from cv2 import *
from numpy import *
import RPi.GPIO as GPIO
import time

f1,f2 = False,False
last_beep = 0

def beep():
	global last_beep
	if int(time.time()-last_beep) > 5:
		print(int(time.time()-last_beep))
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

 
# capture frames from a video
cap1 = VideoCapture(0)
cap2 = VideoCapture(1)
# XML file describing some features of cars
car_cascade = CascadeClassifier('cars.xml')

while True:
    # reads frames from a video boolean return value
    	ret1, frame1 = cap1.read()
        ret2, frame2= cap2.read()
    # convert to gray scale
    	gray1 = cvtColor(frame1, COLOR_BGR2GRAY)
        gray2 = cvtColor(frame2, COLOR_BGR2GRAY)
 
    # Detects cars of different sizes
        cars1= car_cascade.detectMultiScale(gray1, 1.2, 5)  
        cars2= car_cascade.detectMultiScale(gray2, 1.2, 5)	
        print(cars1)
    # To draw a rectangle on each car
        for (x,y,w,h) in cars1 :
            rectangle(frame1,(x,y),(x+w,y+h),(255,255,0),2)
            f1=True
        for (a,b,c,d) in cars2 :
	    rectangle(frame2,(a,b),(a+c,b+d),(0,255,0),2)
            f2=True
     

        if f1 and f2 :
            print("trying to beep1")
			beep()
			f1,f2 = False,False
	
	
   # Display frames in a window 
        namedWindow('cam 1',WINDOW_NORMAL)
        resizeWindow('cam 1',25,25)
        imshow('cam 1', frame1)

        namedWindow('cam 2',WINDOW_NORMAL)
        resizeWindow('cam 2',25,25)
        imshow('cam 2', frame2)	
     
    # Wait for Esc key to stop
        if waitKey(33) == 27:
             break
 
# closes window
destroyAllWindows()

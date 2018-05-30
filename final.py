'''27/2/18  Created by   
			Rithika Chowta 
			Priya Shetty
			Sharan Preetha Noronha'''

from cv2 import *
from RPi.GPIO import *
from time import *

f1, f2, last_beep = False, False, 0  

def beep():			       # called when cars detected on both sides
    global last_beep
    if int(time()-last_beep) > 5:      # to ensure gap of atleast 5 seconds between consecutive beeps
        setmode(BOARD)                 # consider physical location number i.e pin number not GPIO number
        setwarnings(False)             # disables warnings
        setup(11, OUT)                 # buzzer 1
        setup(13, OUT)                 # buzzer 2
        setup(16, OUT)                 # led 1 left
        setup(12, OUT)                 # led 2 right
        setup(38, OUT)		   
	setup(40, OUT)		   
        print("Switching LEDs on")
        print("Switching buzzers on for 5 seconds")
        output(16, HIGH)
        output(12, HIGH)
        output(11, HIGH)
        output(13, HIGH)
        sleep(5)
        output(11, LOW)
        output(13, LOW)
        print("Turning right red off and right green on")
        output(16, LOW)
	output(40, HIGH)
	sleep(5)
	print("Turning left red off and left green on")
	output(12, LOW)
	output(40, LOW)
	output(16, HIGH)
	output(38, HIGH)
	sleep(5)
	print("Turning all off")
        output(38, LOW)
	output(40, LOW)
        last_beep = time()             # updating last beep time
        cleanup()

cap1 = VideoCapture(0)    # capture frames from webcams 0 and 1 
cap2 = VideoCapture(1)

car_cascade = CascadeClassifier('cars.xml')  # XML file describing features of cars 
bike_cascade = CascadeClassifier('bike.xml')  #XML file decribing some features of bikes

while True:
    ret1, frame1 = cap1.read()                # Reads next frame from video and returns boolean value
    ret2, frame2 = cap2.read()

    gray1 = cvtColor(frame1, COLOR_BGR2GRAY)  # Convert to gray scale
    gray2 = cvtColor(frame2, COLOR_BGR2GRAY)

    cars1, rejectlevels1, weights1 = car_cascade.detectMultiScale3(gray1, scaleFactor=1.1,minNeighbors=70,
    minSize=(90,90),maxSize=(270,270),outputRejectLevels=True)
    cars2, rejectlevels2, weights2= car_cascade.detectMultiScale3(gray2, scaleFactor=1.2,minNeighbors=70,
    minSize=(120,120),maxSize=(300,300),outputRejectLevels=True)


    bike1, rejectlevels5, weights5 = bike_cascade.detectMultiScale3(gray1, scaleFactor=1.7,minNeighbors=790,
    minSize=(90,120),maxSize=(200,270),outputRejectLevels=True)
    bike2, rejectlevels6, weights6= bike_cascade.detectMultiScale3(gray2, scaleFactor=1.5,minNeighbors=740,
    minSize=(90,120),maxSize=(200,270),outputRejectLevels=True)
  
    if cars1 is not () or bike1 is not () :
    	 print("Camera 1",str(cars1),str(weights1))
    	 for i in range(len(cars1)):  
		if weights1[i][0] > 1.937:		 # To draw a rectangle on each car from the current frame
			x,y,w,h = cars1[i][0], cars1[i][1], cars1[i][2], cars1[i][3]
			rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 255), 3)
			f1 = True

	 for i in range(len(bike1)):  
		if weights5[i][0] > 3.2:		 # To draw a rectangle on each car from the current frame
			x,y,w,h = bike1[i][0], bike1[i][1], bike1[i][2], bike1[i][3]
			rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 255), 3)
			f1 = True
         

    if cars2 is not () or bike2 is not ():
    	 print("Camera 2",str(cars2),str(weights2))
    	 for i in range(len(cars2)):  
		if weights2[i][0] > 1.937:		 # To draw a rectangle on each car from the current frame
			x,y,w,h = cars2[i][0], cars2[i][1], cars2[i][2], cars2[i][3]
			rectangle(frame2, (x, y), (x+w, y+h), (255, 255, 0), 3)
			f2 = True

	 for i in range(len(bike2)):  
		if weights6[i][0] > 3.2:		 # To draw a rectangle on each car from the current frame
			x,y,w,h = bike2[i][0], bike2[i][1], bike2[i][2], bike2[i][3]
			rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 255), 3)
			f2= True

    print("updating frames")
    namedWindow('Camera 1 - Quantum', WINDOW_NORMAL)    # Displays frame in a 25x25 window
    resizeWindow('Camera 1 - Quantum', 25, 25)
    imshow('Camera 1 - Quantum', frame2)
   
    namedWindow('Camera 2 - Itek', WINDOW_NORMAL)
    resizeWindow('Camera 2 - Itek', 25, 25)
    imshow('Camera 2 - Itek', frame1)

    if f1 and f2:                # If car detected in both frames 
        print("Calling beep")
        beep()
        f1, f2 = False, False	 # Resetting flags

    if waitKey(33) == 27:   # Wait for Esc key to stop
        break
    
destroyAllWindows()   # Closes all windows

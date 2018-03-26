'''27/2/18  Created by   
			Rithika Chowta 
			Priya Shetty
			Sharan Preetha Noronha'''

from cv2 import *
from RPi.GPIO import *
from time import *

f1, f2, last_beep = False, False, 0  ''' flags indicating if car has been detected in video feed from camera 1 and 2 
                                         and initializing variable to indicate timing of last_beep '''

def beep():			                   # called when cars detected on both sides
    global last_beep
    if int(time()-last_beep) > 5:      # to ensure gap of atleast 5 seconds between consecutive beeps
        setmode(BOARD)                 # consider physical location number i.e pin number not GPIO number
        setwarnings(False)             # disables warnings
        setup(11, OUT)                 # buzzer 1
        setup(13, OUT)                 # buzzer 2
        setup(16, OUT)                 # led 1
        setup(12, OUT)                 # led 2
        print("Switching LEDs on")
        print("Switching buzzers on for 5 seconds")
        output(16, HIGH)
        output(12, HIGH)
        output(11, HIGH)
        output(13, HIGH)
        sleep(5)
        output(11, LOW)
        output(13, LOW)
        print("Turning LEDs and buzzers off")
        output(16, LOW)
        output(12, LOW)
        last_beep = time()             # updating last beep time
        cleanup()

cap1 = VideoCapture(0)    # capture frames from webcams 0 and 1 
cap2 = VideoCapture(1)
car_cascade = CascadeClassifier('cascade.xml')  # XML file describing features of cars

while True:
    ret1, frame1 = cap1.read()                # Reads next frame from video and returns boolean value
    ret2, frame2 = cap2.read()
    gray1 = cvtColor(frame1, COLOR_BGR2GRAY)  # Convert to gray scale
    gray2 = cvtColor(frame2, COLOR_BGR2GRAY)
    cars1 = car_cascade.detectMultiScale(gray1, 1.2, 110)  # Detects cars of different sizes
    cars2 = car_cascade.detectMultiScale(gray2, 1.1, 130)
    print(cars1, cars2)
    for (x, y, w, h) in cars1:   # To draw a rectangle on each car from the current frame
        rectangle(frame1, (x, y), (x+w, y+h), (255, 255, 0), 2)
        f1 = True
    for (a, b, c, d) in cars2:
        rectangle(frame2, (a, b), (a+c, b+d), (0, 255, 0), 2)
        f2 = True
    if f1 and f2:                # If car detected in both frames 
        print("Calling beep")
        beep()
        f1, f2 = False, False	 # Resetting flags

    namedWindow('Camera 1 - Quantum', WINDOW_NORMAL)    # Displays frame in a 25x25 window
    resizeWindow('Camera 1 - Quantum', 25, 25)
    imshow('Camera 1 - Quantum', frame1)

    namedWindow('Camera 2 - Itek', WINDOW_NORMAL)
    resizeWindow('Camera 2 - Itek', 25, 25)
    imshow('Camera 2 - Itek', frame2)

    if waitKey(33) == 27:   # Wait for Esc key to stop
        break
    
destroyAllWindows()   # Closes all windows

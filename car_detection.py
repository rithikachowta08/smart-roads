''' OpenCV Python program to detect cars in video '''
from cv2 import *
from fps_module import FPS


cap = VideoCapture(0)                                        # capture frames from a video
fps = FPS().start()
#cap = VideoCapture("video.avi") 
car_cascade = CascadeClassifier('xmls/bike.xml')               # XML file describing some features of cars

while True:
    ret, next_frame = cap.read()                              # reads frames from a video boolean return value
    gray = cvtColor(next_frame, COLOR_BGR2GRAY)               # convert to gray scale
    next_frame = flip(next_frame,1)                           # cause the camera was being weird and flipped
    cars = car_cascade.detectMultiScale(gray, 1.1, 20)        # Detects cars of different sizes
    for (x,y,w,h) in cars:
        rectangle(next_frame,(x,y),(x+w,y+h),(0,0,255),2)     # To draw a rectangle on each car
    imshow('video', next_frame)                               # Display frames in a window 
    if waitKey(1) == 27:                                      # Wait for Esc key to stop
        break
    fps.update()

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

destroyAllWindows()                                           # closes windows
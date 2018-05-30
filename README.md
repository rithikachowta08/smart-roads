# Smart Roads - Real time Vehicle Collision Prevention System
Final year CS project - Rithika, Priya, Sharan

## Hardware Pre-requisites:

- Raspberry Pi 3 B

- 16 GB, class 10 Sandisk microSD card

- USB webcameras x 2

- Red LEDs x 2

- 330Ω Resistors x 2

- Green LEDs x 2

- Buzzers x 2

- Powered USB hub

- Jumper wires to connect the GPIO components

- Mouse, keyboard, monitor

## Software Pre-requisites:

- Python 3

- OpenCV 3.3.0

- Raspbian Stretch 

## Methodology:

Vehicles speeding along a blind curve are not aware of the presence of vehicles coming from the other direction. Here, a system is proposed to alert drivers going around a blind curve to the presence of oncoming vehicles.

- Cameras, green and red LED warning lights and piezoelectric buzzers are mounted on a pole on each side of the curve, which are connected to a Raspberry Pi 3 B.

- XML Classifiers for cars and bikes are generated using LBP Cascade training. The live video feed from the two cameras placed on either side of the curve is given to an OpenCV algorithm to detect presence of vehicles. 

- If vehicles are detected on both sides of the curve at the same time, the buzzers and red lights are activated, thus alerting the drivers.

- Green LEDs are used to coordinate their movement so as to resolve confusion.

- Concepts used include **IoT, machine learning** and **computer vision**.

## [Demo](https://www.youtube.com/watch?v=JA7LK_PBREA) 

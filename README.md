# Smart Roads - Real time Vehicle Collision Prevention System
Final year CS project - Rithika, Priya, Sharan

## Methodology:

Vehicles speeding along a blind curve are not aware of the presence of vehicles coming from the other direction. Here, a system is proposed to alert drivers going around a blind curve to the presence of oncoming vehicles.

- Cameras, green and red LED warning lights and piezoelectric buzzers are mounted on a pole on each side of the curve, which are connected to a Raspberry Pi 3 B.

- XML Classifiers for cars and bikes are generated using LBP Cascade training. The live video feed from the two cameras placed on either side of the curve is given to an OpenCV algorithm to detect presence of vehicles. 

- If vehicles are detected on both sides of the curve at the same time, the buzzers and red lights are activated, thus alerting the drivers.

- Green LEDs are used to coordinate their movement so as to resolve confusion.

- Concepts used include **IoT, machine learning** and **computer vision**.

## [Demo](https://www.youtube.com/watch?v=JA7LK_PBREA) 

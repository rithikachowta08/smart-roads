# smart-roads
Final year CS project - Rithika, Priya, Sharan

Abstract:
Blind curves are one of the leading causes of road accidents. Vehicles speeding along a curve are not aware of the presence of vehicles 
coming from the other direction. Here, a system is proposed to alert drivers going around a blind curve to the presence of oncoming 
vehicles. 2 poles are erected on either side of the curve, bearing cameras, red and green LED lights and piezoelectric buzzers. They are connected to a Raspberry Pi. The live video feed from the cameras is processed to detect the presence of vehicles. If vehicles are approaching on both sides of the curve, the buzzers and red lights are activated, thus alerting the drivers of the vehicle to slow down. Then the green LED is activated on one side to allow one vehicle to move forward. After it passes, the other vehicle is allowed to move by activating the green LED on the other side. Red LED is reactivated on the previous side, to stop any vehicles that were behind the first vehicle. After all vehicles pass, all LEDs are deactivated.

Our area of study includes IoT, machine learning and computer vision.

Methodology:
Vehicles speeding along a curve are not aware of the presence of vehicles coming from the other direction. Here, a system is proposed to alert drivers going around a blind curve to the presence of oncoming vehicles.
• Cameras, LED warning lights and piezoelectric buzzers are mounted on a pole which is then connected to a Raspberry Pi and video from the cameras is processed to detect oncoming vehicles.
• XML Classifiers for cars, trucks and bikes are generated using LBP Cascade training. The live video feed from two cameras placed on either side of the curve is given to the OpenCV algorithm to detect presence of vehicles. If vehicles approaching on both the sides of the curve are detected, the buzzers and lights are activated, thus alerting the drivers to be aware of the incoming vehicle. Once they are alerted with red LEDs, one of the two green LEDs will glow indicating that particular vehicle to move.
• The red LEDs and buzzers will be switched on for specified amount of time indicating the sign of warning the driver and then green LEDs will glow to let vehicles to cross depending on the program.

For demo, please visit https://www.youtube.com/watch?v=JA7LK_PBREA

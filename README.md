# Fire-Detection

A project in which a system was developed to monitor real-time video and generate an alert if a fire is detected in the video feed. 

__Tools Used:__
* Raspberry Pi 3
* Raspberry Pi Camera
* Python 3
* OpenCV library (Python)
* Firebase
* Raspbian OS (Debian-based Linux distribution Operating System)

__Description__:

The project used a Raspberry Pi 3 with a PiCam to provide the live video feed to be monitored. A python program using the OpenCV image processing library takes this live feed and using image processing techniques, determines whether there is a fire in the video feed or not. 
If a fire is detected, the Raspberry Pi can generate a visual or audible alarm at the site using an alarm light or speaker. 
The Python program is also integrated with a Firebase server, to which an alert is updated which sends a alert notification to the users connected to this database using an Android application to alert the users that a fire has erupted at the site being monitored.
This system can be used as a low-cost safety mechanism in laboratories or factories by integrating this system with the live CCTV feeds of the rooms.

## Cone-Winder-Control-Software
The Cone Winder Control Software is a demonstration project for makers and hobbyists to control a cone winder via an Arduino. The software features a graphical user interface (GUI) for configuring winding parameters and sending commands to the Arduino. This tool is not a finalized product but rather a working example that shows how such a system could be implemented.
The construction of the cone winder is based on the principles of Schönflies Motion, while the motion control leverages Bresenham's Line Algorithm.

# Features
- GUI Interface: Allows users to input parameters for winding patterns.
- Templates: Provides pre-defined templates for cone and cylinder winding.
- Arduino Communication: Sends commands to an Arduino via serial communication.
- Customizable: Input fields for setting offsets, positions, repeat counts, and step intervals.

# Requirements
To use this software, ensure you have the following:

# Hardware:
Arduino board (e.g., Arduino Uno or compatible)
Cone winder hardware setup (My cone winder project is published on Hackaday: https://hackaday.io/projects/hacker/382663)

# Usage
- Launch the application by running the script: python main.py
- Enter the required parameters for your cone winder in the GUI.
- Define your own templates according to your cone winder.
- Test the parameters of the templates.
- Click SEND TO ARDUINO to transfer data to the Arduino.
- Monitor the communication and ensure data is processed correctly.

# Notes
- The success of the system depends on the specific construction of your cone winder and the cones you use.
- Ensure that all motors have enough power and the Arduino is connected to the correct COM port before starting the application.
- For detailed troubleshooting, refer to the console logs.
- Sensors to stop the motor have not yet been implemented in the cone winder hardware, and corresponding code is missing from this software. Use the system with caution and manual supervision.

# Limitations
- This software is not a production-ready solution.
- It is provided as-is for educational and demonstration purposes.

# License
This software is released under an open-source license. Feel free to modify and use it for your projects. Contributions and suggestions are welcome!

# Acknowledgments
- The concept of Schönflies Motion inspired the design of the cone winder, see example on Youtube: https://www.youtube.com/shorts/_nzxGOKhHSY 
- Motion control is implemented using Bresenham's Line Algorithm.

Author
Irene Wolf

"""
Cone Winder Control Software
Developed by: Irene Wolf
Date: Version 19.12.24
Purpose: Demonstration of a cone winder control system for makers and hobbyists.


This program demonstrates how to control a cone winder using an Arduino and a simple graphical user interface (GUI).
It is primarily aimed at makers and hobbyists who want to experiment with cone winding and explore possible implementations.

**Important Notes:**
- The construction of the cone winder is based on the principles of "Schönflies Motion".
- The motion control for the machine relies on "Bresenham's line algorithm" to ensure accurate and efficient stepper motor movements.
- This software is not a finalized product but serves as a foundation for further development and customization.
- Included templates provide examples, but users need to adapt parameters based on their specific cone winder design and the cones they are using.

**Key Features:**
- Predefined templates for cone winding configurations.
- Customizable parameter entry to accommodate various machine setups.
- Serial communication with an Arduino for precise command execution.

This program is a starting point for building and modifying your own cone winder control system, tailored to your specific project needs.


"""

# Import required libraries
import random, sys  # For random operations and system-level functions
import PyCmdMessenger  # For communication with Arduino
from PyQt5 import QtCore, QtGui, QtWidgets  # For GUI creation using PyQt5

print("GUI Version 19.12.24")

# Define the main GUI class
class Ui_MainWindow(object):

    # Define a list of commands to communicate with the Arduino
    commands = [["multi_ping", 'i*'], ["multi_pong", 'i*'], ["pattern_send", 'i']]

    # Initialize the Arduino board and command messenger
    arduino = PyCmdMessenger.ArduinoBoard('COM4', 115200)  # Arduino on COM4 with baud rate 115200
    cmdmessenger = PyCmdMessenger.CmdMessenger(arduino, commands)  # Link commands to Arduino

    # Function to fill form fields with default values for a cone pattern
    def cone_template(self):
        self.x_offset.insert("0")
        self.y_offset.insert("0")
        self.x_pos_to_go.insert("-3500")
        self.y_pos_to_go.insert("350")
        self.repeat.insert("2")
        self.z_steps.insert("199")
        self.z_repeat_steps.insert("5")
        self.interval_z.insert("40")
        self.interval_xy.insert("40")

    # Function to fill form fields for a cylinder pattern (not implemented)
    def zylinder_template(self):
        pass

    # Function to clear all form fields
    def clear_data(self):
        self.x_offset.clear()
        self.y_offset.clear()
        self.x_pos_to_go.clear()
        self.y_pos_to_go.clear()
        self.repeat.clear()
        self.z_steps.clear()
        self.z_repeat_steps.clear()
        self.interval_z.clear()
        self.interval_xy.clear()

    pos_and_repeat = []  # Store the entered data for processing

    # Function to read and store data from input fields
    def set_data(self):
        print("start, ")
        try:
            # Read and parse integer values from the input fields
            num1 = int(self.x_offset.text()), int(self.y_offset.text()), int(self.x_pos_to_go.text()), int(self.y_pos_to_go.text()), int(self.repeat.text())
            num2 = int(self.z_steps.text()), int(self.z_repeat_steps.text()), int(self.interval_z.text()), int(self.interval_xy.text())
            self.pos_and_repeat = num1 + num2  # Combine into a single tuple
            print("numbers:", self.pos_and_repeat)  # Print the captured data
        except ValueError:
            print("Value error")  # Handle invalid inputs

    # Function to print the stored data
    def print_data(self):
        print("Data: ", self.pos_and_repeat)

    # Function to send data to the Arduino and verify the response
    def send_data_to_arduino(self):
        print("send to Arduino: ", self.pos_and_repeat)
        num_args = int(len(self.pos_and_repeat))  # Get the number of arguments to send
        try:
            # Send the data using the "multi_ping" command
            self.cmdmessenger.send("multi_ping", num_args, *self.pos_and_repeat[:])
            print("first")

            # Receive the response from Arduino
            received_cmd = self.cmdmessenger.receive()
            print(received_cmd)  # Print the full response
            received = received_cmd[1]  # Extract the payload
            print(received)

            # Verify if sent data matches received data
            success = 1
            for i in range(num_args):
                if self.pos_and_repeat[i] == received[i]:
                    success *= 1  # Success
                else:
                    success = 0  # Failure
                if success == 0:
                    success = "FAIL"
                else:
                    success = "PASS"

            print("success", success)  # Output success status
        except:
            print("No value")  # Handle exceptions

    # Function to stop the process on the Arduino (not implemented)
    def stopp_prozess_arduino(self):
        pass

    # Function to set up the GUI
    def setupUi(self, MainWindow):
        # Configure main window properties
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 578)
        MainWindow.setStyleSheet("font: 87 14pt \"Arial\";")
        MainWindow.setWindowTitle("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Font settings for GUI elements
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)

        # Define labels, text fields, and buttons
        # Each section initializes a widget, sets its properties, and adds it to the main window
        # The pattern is repeated for multiple GUI elements, so they are not individually explained here
        # ...
        # Set up the event handlers for buttons using `.clicked.connect` to link them with their respective functions
        # ...

        self.label_x_offset = QtWidgets.QLabel(self.centralwidget)
        self.label_x_offset.setGeometry(QtCore.QRect(50, 20, 150, 30))
        self.label_x_offset.setFont(font)
        self.label_x_offset.setObjectName("label_x_offset")
        self.label_x_offset.setText("X offset")

        self.x_offset = QtWidgets.QLineEdit(self.centralwidget)
        self.x_offset.setGeometry(QtCore.QRect(210, 20, 150, 30))
        self.x_offset.setFont(font)
        self.x_offset.setObjectName("x_offset")

        self.label_y_offset = QtWidgets.QLabel(self.centralwidget)
        self.label_y_offset.setGeometry(QtCore.QRect(50, 60, 150, 30))
        self.label_y_offset.setFont(font)
        self.label_y_offset.setObjectName("label_y_offset")
        self.label_y_offset.setText("Y offset")

        self.y_offset = QtWidgets.QLineEdit(self.centralwidget)
        self.y_offset.setGeometry(QtCore.QRect(210, 60, 150, 30))
        self.y_offset.setFont(font)
        self.y_offset.setObjectName("y_offset")

        self.label_x_pos = QtWidgets.QLabel(self.centralwidget)
        self.label_x_pos.setGeometry(QtCore.QRect(50, 100, 150, 30))
        self.label_x_pos.setFont(font)
        self.label_x_pos.setObjectName("label_x_pos")
        self.label_x_pos.setText("x pos to go")

        self.x_pos_to_go = QtWidgets.QLineEdit(self.centralwidget)
        self.x_pos_to_go.setGeometry(QtCore.QRect(210, 100, 150, 30))
        self.x_pos_to_go.setFont(font)
        self.x_pos_to_go.setObjectName("x_pos_to_go")

        self.label_y_pos = QtWidgets.QLabel(self.centralwidget)
        self.label_y_pos.setGeometry(QtCore.QRect(50, 140, 150, 30))
        self.label_y_pos.setFont(font)
        self.label_y_pos.setObjectName("label_y_pos")
        self.label_y_pos.setText("y pos to go")

        self.y_pos_to_go = QtWidgets.QLineEdit(self.centralwidget)
        self.y_pos_to_go.setGeometry(QtCore.QRect(210, 140, 150, 30))
        self.y_pos_to_go.setFont(font)
        self.y_pos_to_go.setObjectName("y_pos_to_go")

        self.label_repeat = QtWidgets.QLabel(self.centralwidget)
        self.label_repeat.setGeometry(QtCore.QRect(50, 180, 150, 30))
        self.label_repeat.setFont(font)
        self.label_repeat.setObjectName("label_repeat")
        self.label_repeat.setText("Repeat")

        self.repeat = QtWidgets.QLineEdit(self.centralwidget)
        self.repeat.setGeometry(QtCore.QRect(210, 180, 150, 30))
        self.repeat.setObjectName("Repeat")

        self.label_z_steps = QtWidgets.QLabel(self.centralwidget)
        self.label_z_steps.setGeometry(QtCore.QRect(670, 20, 150, 30))
        self.label_z_steps.setFont(font)
        self.label_z_steps.setObjectName("label_z_turn")
        self.label_z_steps.setText("Z steps")

        self.z_steps = QtWidgets.QLineEdit(self.centralwidget)
        self.z_steps.setGeometry(QtCore.QRect(830, 20, 150, 30))
        self.z_steps.setFont(font)
        self.z_steps.setObjectName("z_steps")

        self.label_z_repeat_steps = QtWidgets.QLabel(self.centralwidget)
        self.label_z_repeat_steps.setGeometry(QtCore.QRect(670, 60, 150, 30))
        self.label_z_repeat_steps.setFont(font)
        self.label_z_repeat_steps.setObjectName("label_z_turn_repeat")
        self.label_z_repeat_steps.setText("Z repeat steps")

        self.z_repeat_steps = QtWidgets.QLineEdit(self.centralwidget)
        self.z_repeat_steps.setGeometry(QtCore.QRect(830, 60, 150, 30))
        self.z_repeat_steps.setFont(font)
        self.z_repeat_steps.setObjectName("z_repeat_steps")

        self.label_interval_z = QtWidgets.QLabel(self.centralwidget)
        self.label_interval_z.setGeometry(QtCore.QRect(670, 100, 150, 30))
        self.label_interval_z.setFont(font)
        self.label_interval_z.setObjectName("label_interval_z")
        self.label_interval_z.setText("Interval Z")

        self.interval_z = QtWidgets.QLineEdit(self.centralwidget)
        self.interval_z.setGeometry(QtCore.QRect(830, 100, 150, 30))
        self.interval_z.setFont(font)
        self.interval_z.setObjectName("interval_z")

        self.label_interval_xy = QtWidgets.QLabel(self.centralwidget)
        self.label_interval_xy.setGeometry(QtCore.QRect(670, 140, 150, 30))
        self.label_interval_xy.setFont(font)
        self.label_interval_xy.setObjectName("label_interval_xy")
        self.label_interval_xy.setText("Interval XY")

        self.interval_xy = QtWidgets.QLineEdit(self.centralwidget)
        self.interval_xy.setGeometry(QtCore.QRect(830, 140, 150, 30))
        self.interval_xy.setFont(font)
        self.interval_xy.setObjectName("interval_xy")

        self.button_cone_template = QtWidgets.QPushButton(self.centralwidget)
        self.button_cone_template.setGeometry(QtCore.QRect(400, 20, 230, 50))
        self.button_cone_template.setFont(font)
        self.button_cone_template.setDefault(True)
        self.button_cone_template.setObjectName("button_cone_template")
        self.button_cone_template.setText("Cone 160 mm Template")
        self.button_cone_template.clicked.connect(self.cone_template)

        self.button_zylinder_template = QtWidgets.QPushButton(self.centralwidget)
        self.button_zylinder_template.setGeometry(QtCore.QRect(400, 80, 230, 50))
        self.button_zylinder_template.setFont(font)
        self.button_zylinder_template.setDefault(True)
        self.button_zylinder_template.setObjectName("button_zylinder_template")
        self.button_zylinder_template.setText("Zylinder template")
        self.button_zylinder_template.clicked.connect(self.zylinder_template)

        self.button_clear_data = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear_data.setGeometry(QtCore.QRect(670, 200, 230, 50))
        self.button_clear_data.setFont(font)
        self.button_clear_data.setDefault(True)
        self.button_clear_data.setObjectName("button_clear_data")
        self.button_clear_data.setText("CLEAR DATA")
        self.button_clear_data.clicked.connect(self.clear_data)

        self.button_set_data = QtWidgets.QPushButton(self.centralwidget)
        self.button_set_data.setGeometry(QtCore.QRect(50, 300, 230, 50))
        self.button_set_data.setFont(font)
        self.button_set_data.setDefault(True)
        self.button_set_data.setObjectName("button_set_data")
        self.button_set_data.setText("SET DATA")
        self.button_set_data.clicked.connect(self.set_data)

        self.button_print_data = QtWidgets.QPushButton(self.centralwidget)
        self.button_print_data.setGeometry(QtCore.QRect(320, 300, 230, 50))
        self.button_print_data.setFont(font)
        self.button_print_data.setCheckable(False)
        self.button_print_data.setDefault(True)
        self.button_print_data.setObjectName("button_print_data")
        self.button_print_data.setText("PRINT DATA")
        self.button_print_data.clicked.connect((self.print_data))

        self.button_send_to_arduino = QtWidgets.QPushButton(self.centralwidget)
        self.button_send_to_arduino.setGeometry(QtCore.QRect(590, 300, 230, 50))
        self.button_send_to_arduino.setFont(font)
        self.button_send_to_arduino.setCheckable(False)
        self.button_send_to_arduino.setDefault(True)
        self.button_send_to_arduino.setObjectName("button_send_to_arduino")
        self.button_send_to_arduino.setText("SEND TO ARDUINO")
        self.button_send_to_arduino.clicked.connect(self.send_data_to_arduino)

        self.button_stopp = QtWidgets.QPushButton(self.centralwidget)
        self.button_stopp.setGeometry(QtCore.QRect(670, 420, 230, 50))
        self.button_stopp.setFont(font)
        self.button_stopp.setCheckable(False)
        self.button_stopp.setDefault(True)
        self.button_stopp.setObjectName("button_stopp")
        self.button_stopp.setText("S T O P P")
        self.button_stopp.clicked.connect(self.stopp_prozess_arduino)

        self.ok_abbrechen = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.ok_abbrechen.setGeometry(QtCore.QRect(50, 410, 140, 81))
        self.ok_abbrechen.setStyleSheet("font: 16pt \"Arial\";")
        self.ok_abbrechen.setOrientation(QtCore.Qt.Vertical)
        self.ok_abbrechen.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.ok_abbrechen.setObjectName("ok_abbrechen")

        # Configure additional GUI elements like menubar, statusbar, and dialog buttons
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 44))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setTitle("Eingabemaske")
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())

# Main entry point of the program
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # Initialize PyQt application
    MainWindow = QtWidgets.QMainWindow()  # Create main window
    ui = Ui_MainWindow()  # Instantiate the UI class
    ui.setupUi(MainWindow)  # Set up the GUI
    MainWindow.show()  # Show the main window

    sys.exit(app.exec())  # Start the application loop

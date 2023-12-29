"""
Project: Charty Robot
Date: 2023-10-23
Version: 0.1
Author: Hugo Nilsson

Main window and its buttons.
"""
from tkinter import * # Useful library for GUI creation

# Declare window
window = Tk()

# This creates a window, called frame from the window object declared above.
frame = Frame(window, width=800, height=800, bg="lightgrey")
window.title("ChartyBot Interface Ver 0.1")

frame.pack()

button_pressed = IntVar()

def enableInput():
    inputBox.configure(state=NORMAL)
    print("Input enabled.")

# Disables input into inputBox when called
def disableInput():
    inputBox.delete(1.0, END)
    inputBox.configure(state=DISABLED)
    print("Input disabled.")

# Function for retrieving input from inputBox
# Waits until the global variable button_pressed becomes "pressed" before progressing in the code.
def getInput():
    disableAllButtons()
    enterInputButton.wait_variable(button_pressed)
    print("finished waiting")
    
    """ if validateInput():
        input = inputBox.get(1.0, END)
        enableAllButtons()
        print("Hello")
        return input """
    
    input = inputBox.get(1.0, END)
    enableAllButtons()
    return input

""" def validateInput():
    input = inputBox.get(1.0, END)
    if input:
        try:
            print("Correct Input")
            float(input)
            return True
        except ValueError:
            print("Wrong Input")
            return False
    else:
        return "uegghhh" """

# Binds the following keys: ARROW_UP, ARROW_RIGHT, ARROW_LEFT, ARROW_DOWN to respective functions that each sends
# a signal to the robot for manual control.
def enableListening():
    enableManualControl.configure(state=DISABLED)
    
    window.bind("<Up>", driveFwd)
    window.bind("<Down>", driveReverse)
    window.bind("<Left>", driveLeft)
    window.bind("<Right>", driveRight)

    disableAllButtons()
    
    disableManualControl.configure(state=NORMAL)

# Like above, but instead Un-Binds each button so that the robot can't be controlled unless the enableListening is active. 
def disableListening():
    disableManualControl.configure(state=DISABLED)

    window.unbind("<Up>")
    window.unbind("<Down>")
    window.unbind("<Left>")
    window.unbind("<Right>")
    
    enableAllButtons()
    
    enableManualControl.configure(state=NORMAL)
################################# FUNCTIONS ############################################################################
# Listens to keypresses when active. Event-parameter seems useless since it is greyed out but is required for functions to work. 
def driveFwd(event):
    print("Up arrow pressed")
    return

def driveReverse(event):
    print("Down Arrow Pressed")
    return

def driveLeft(event):
    print("Left Arrow Pressed")
    return

def driveRight(event):
    print("Right Arrow Pressed")
    return

# Calibrational functions. Enter value in client of actual distance to object on respective side. 
def calibrateFwd():
    enableInput()
    print("Calibrate Forward Pointing Sensor")
    result = getInput()
    print(result)
    disableInput()
    return

def calibrateLeft():
    enableInput()
    print("Calibrate Left")
    result = getInput()
    print(result)
    disableInput()
    return

def calibrateRight():
    enableInput()
    print("Calibrate Right")
    result = getInput()
    print(result)
    disableInput()
    return

# Disables all buttons when entering a value to prevent any potential errors that pressing two different buttons while program is waiting for input.
def disableAllButtons():
    doCalDistanceL.configure(state=DISABLED)
    doCalDistanceR.configure(state=DISABLED)
    doCalDistanceFwd.configure(state=DISABLED)
    doQuitButton.configure(state=DISABLED)
    enableManualControl.configure(state=DISABLED)

def enableAllButtons():
    doCalDistanceL.configure(state=NORMAL)
    doCalDistanceR.configure(state=NORMAL)
    doCalDistanceFwd.configure(state=NORMAL)
    doQuitButton.configure(state=NORMAL)
    enableManualControl.configure(state=NORMAL)


#################################### CONTROLS #######################################################################
# Create the window for the buttons to reside in.
buttonsFrame = Frame(window, width=325, height=750, bg="darkgrey", highlightbackground="black", highlightthickness=2)
#buttonsFrame.title("User Input")
buttonsFrame.place(x=455, y=25)

# Stops the below LABEL from shrinking its parent to fit its size.
buttonsFrame.pack_propagate(False)

buttonLabel = Label(buttonsFrame, text="Controls").pack()

doQuitButton = Button(buttonsFrame, text="Quit", command=frame.quit, width=15)
doQuitButton.place(x=200, y=220)

# Calibration controls
doCalDistanceL = Button(buttonsFrame, text="Calibrate left \ndistance-reading \nsensor", state=NORMAL, width=15, command=calibrateLeft) # Calibrate left distance-reading sensor
doCalDistanceL.place(x=10, y=160)

doCalDistanceR = Button(buttonsFrame, text="Calibrate right \ndistance-reading \nsensor", state=NORMAL, width=15,  command=calibrateRight) # Calibrate right distance-reading sensor
doCalDistanceR.place(x=200, y=160)

doCalDistanceFwd = Button(buttonsFrame, text="Calibrate \nforward-reading\nsensor", state=NORMAL, width=15, command=calibrateFwd) # Calibrates forward-pointed distance-reading sensor.
doCalDistanceFwd.place(x=10, y=220)

# Enables manual control
enableManualControl = Button(buttonsFrame, text="Enable manual\n control", state=NORMAL, width=15, command=enableListening) # Calibrates forward-pointed distance-reading sensor.
enableManualControl.place(x=10, y=30)

disableManualControl = Button(buttonsFrame, text="Disable manual\n control", state=DISABLED, width=15, command=disableListening) # Calibrates forward-pointed distance-reading sensor.
disableManualControl.place(x=10, y=75)

# Creates a text-box for inputting values
inputBox = Text(buttonsFrame, width=15, height=1, state=DISABLED)
inputBox.place(x=95, y=720)

# Enter Value for inputbox
enterInputButton = Button(buttonsFrame, width=10, height=1, text="Enter Value", command=lambda: button_pressed.set("pressed"))
enterInputButton.place(x=10, y=718)

#################################### UNIT FEEDBACK ###################################################################

# Create a window for showing sensor statuses etc. Has to be a canvas since it constantly will be updated with readings from on-board sensors.
sensorFrame = Canvas(window, width=400, height=320, bg="darkgrey", highlightbackground="black", highlightthickness=2)
sensorFrame.place(x=25, y=455)

# Labels for info
distanceFwdLabel = Label(sensorFrame, width=12, anchor="w", text="Distance Fwd: ")
distanceFwdLabel.place(x=10, y=40)

distanceLeftLabel = Label(sensorFrame, width=12, anchor="w", text="Distance Left: ")
distanceLeftLabel.place(x=10, y=70)

distanceRightLabel = Label(sensorFrame, width=12, anchor="w", text="Distance Right: ")
distanceRightLabel.place(x=10, y=100)

connectionStatusLabel = Label(sensorFrame, width=15, anchor="w", text="Connection Status: ")
connectionStatusLabel.place(x=10, y=290)

# Stops sensorFrame from shrinking its parent, frame, to fit its size.
sensorFrame.pack_propagate(False)

sensorLabel = Label(sensorFrame, text="Unit Feedback").pack()

################################## MAP #################################################################################
# This creates a canvas, and places it inside the frame. Frames are different from windows in that can be drawn in, which a window cannot. Will be useful for displaying the map later on.
mapWindow = Canvas(frame, width=400, height=400, bg="white", highlightbackground="black", highlightthickness=2)
mapWindow.place(x=25, y=25)

frame.mainloop()


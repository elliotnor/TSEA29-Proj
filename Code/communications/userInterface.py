"""
Project: Charty Robot
Date: 2023-10-23
Version: 0.1
Author: Hugo Nilsson

Main window and its buttons.
"""

from tkinter import * # Useful library for GUI creation
import os
import server
import mapping

os.system('xset r off')

noKey = "0000" 
fwd = 0
down = 0
left = 0
right = 0
connectionSuccessful = 0
windowColor = "bisque1"
buttonColor = "darkkhaki"
borderColor = "tan4"

#local_server, client, addr = server.setup_server()

# Declare window
window = Tk()

# This creates a window, called frame from the window object declared above.
frame = Frame(window, width=800, height=800, bg="antiquewhite1", highlightcolor="white", highlightbackground="white")
window.title("ChartyBot Interface Ver 1.0")

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
    
    window.bind("<KeyPress-Up>", fwdPressed)
    window.bind("<KeyRelease-Up>", fwdReleased)
    window.bind("<KeyPress-Down>", downPressed)
    window.bind("<KeyRelease-Down>", downReleased)
    window.bind("<KeyPress-Left>", leftPressed)
    window.bind("<KeyRelease-Left>", leftReleased)
    window.bind("<KeyPress-Right>", rightPressed)
    window.bind("<KeyRelease-Right>", rightReleased)

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
def fwdPressed(event):
    result = "0"
    id_fwd = "0001"
    print("up arrow pressed")
    data = createBinResult(result, id_fwd)
    server.tell_client(client, data)
    return

def fwdReleased(event):
    print("up arrow released")
    result = "0"
    id = noKey
    data = createBinResult(result, id)
    server.tell_client(client, data)
    return

def downPressed(event):
    print("Down Arrow Pressed")
    result = "0"
    id_down = "0010"
    data = createBinResult(result, id_down)
    server.tell_client(client, data)
    return

def downReleased(event):
    result = "0"
    id = noKey
    data = createBinResult(result, id)
    server.tell_client(client, data)
    return

def leftPressed(event): 
    print("Left Key Pressed")
    result = "0"
    id_left = "0011"
    data = createBinResult(result, id_left)
    server.tell_client(client, data)
    return

def leftReleased(event):
    result = "0"
    id = noKey
    data = createBinResult(result, id)
    server.tell_client(client, data)
    return

def rightPressed(event):
    print("Right Key Pressed")
    result = "0"
    id_right = "0100"
    data = createBinResult(result, id_right)
    server.tell_client(client, data)
    return

def rightReleased(event):
    result = "0"
    id = noKey
    data = createBinResult(result, id)
    server.tell_client(client, data)
    return

# Calibrational functions. Enter value in client of actual distance to object on respective side. 
def calibrateFwd():
    enableInput()
    print("Calibrate Forward Pointing Sensor")
    result = bin(int(getInput()))
    id_fwd = "1000"
    data = createBinResult(result, id_fwd)
    server.tell_client(client, data)
    disableInput()
    return

def calibrateLeft():
    enableInput()
    print("Calibrate Left")
    result = bin(int(getInput()))
    id_left = "0101"
    data = createBinResult(result, id_left)
    server.tell_client(client, data)
    disableInput()
    return

def calibrateRight():
    enableInput()
    result = bin(int(getInput()))
    id_right = "0110"
    data = createBinResult(result, id_right)
    server.tell_client(client, data)
    disableInput()
    return

def createBinResult(result, id):
    #"0b_xxxx_xx_xxxxxxxx", id_xx_val
    data = id + "00"
    seq1 = '0' * 10
    data += bin(int(seq1, 2) | int(result, 2))[2:].zfill(10)
    return data


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
buttonsFrame = Frame(window, width=325, height=750, bg=windowColor, highlightbackground=borderColor, highlightthickness=2)
#buttonsFrame.title("User Input")
buttonsFrame.place(x=450, y=25)

# Stops the below LABEL from shrinking its parent to fit its size.
buttonsFrame.pack_propagate(False)

buttonLabel = Label(buttonsFrame, text="Controls", font="Times 18", bg=windowColor).pack()

doQuitButton = Button(buttonsFrame, text="Quit", command=frame.quit, width=15, font="Times 12", bg="lightsalmon1")
doQuitButton.place(x=170, y=707)

# Calibration controls
doCalDistanceL = Button(buttonsFrame, text="Calibrate left \ndistance-reading \nsensor", state=NORMAL, width=15, command=calibrateLeft, font="Times 12", bg=buttonColor) # Calibrate left distance-reading sensor
doCalDistanceL.place(x=10, y=230)

doCalDistanceR = Button(buttonsFrame, text="Calibrate right \ndistance-reading \nsensor", state=NORMAL, width=15,  command=calibrateRight, font="Times 12", bg=buttonColor) # Calibrate right distance-reading sensor
doCalDistanceR.place(x=170, y=230)

doCalDistanceFwd = Button(buttonsFrame, text="Calibrate \nforward-reading\nsensor", state=NORMAL, width=15, command=calibrateFwd, font="Times 12", bg=buttonColor) # Calibrates forward-pointed distance-reading sensor.
doCalDistanceFwd.place(x=92, y= 150)

# Enables manual control
enableManualControl = Button(buttonsFrame, text="Enable manual\n control", state=NORMAL, width=15, command=enableListening, font="Times 12", bg=buttonColor) # Calibrates forward-pointed distance-reading sensor.
enableManualControl.place(x=10, y=40)

disableManualControl = Button(buttonsFrame, text="Disable manual\n control", state=DISABLED, width=15, command=disableListening, font="Times 12", bg=buttonColor) # Calibrates forward-pointed distance-reading sensor.
disableManualControl.place(x=170, y=40)

# Creates a text-box for inputting values
inputBox = Text(buttonsFrame, width=10, height=1, state=NORMAL)
inputBox.place(x=115, y=326)

# Enter Value for inputbox
enterInputButton = Button(buttonsFrame, width=10, height=1, text="Enter Value", command=lambda: button_pressed.set("pressed"), font="Times 12", bg=buttonColor)
enterInputButton.place(x=10, y=320)

#################################### UNIT FEEDBACK ###################################################################

# Create a window for showing sensor statuses etc. Has to be a canvas since it constantly will be updated with readings from on-board sensors.
sensorFrame = Frame(window, width=403, height=320, bg=windowColor, highlightbackground=borderColor, highlightthickness=2)
sensorFrame.place(x=25, y=455)

# Labels for info
distanceFwdLabel = Label(sensorFrame, width=12, anchor="w", text="Distance Fwd: ", font="Times 12", bg=windowColor)
distanceFwdLabel.place(x=10, y=40)

distanceFwdData = Label(sensorFrame, width=6, anchor="w", text="0 cm", font="Times 12", bg=windowColor)
distanceFwdData.place(x=110, y=40)

distanceLeftLabel = Label(sensorFrame, width=12, anchor="w", text="Distance Left: ", font="Times 12", bg=windowColor)
distanceLeftLabel.place(x=10, y=70)

distanceLeftData = Label(sensorFrame, width=6, anchor="w", text="0 cm", font="Times 12", bg=windowColor)
distanceLeftData.place(x=110, y=70)

distanceRightLabel = Label(sensorFrame, width=12, anchor="w", text="Distance Right: ", font="Times 12", bg=windowColor)
distanceRightLabel.place(x=10, y=100)

distanceRightData = Label(sensorFrame, width=6, anchor="w", text="0 cm", font="Times 12", bg=windowColor)
distanceRightData.place(x=110, y=100)

connectionStatusLabel = Label(sensorFrame, width=15, anchor="w", text="Connection Status: ", font="Times 12", bg=windowColor)
connectionStatusLabel.place(x=10, y=285)

connectionStatusText = Label(sensorFrame, width=10, anchor="w", text=" Disconected", font="Times 12", bg="lightsalmon1")
connectionStatusText.place(x=132, y=285)

distance_data = 100
# Update distance data
def updateFwdDataLabel():
    data = str(distance_data) + " cm"
    distanceFwdData.configure(text=data)

def updateLeftDataLabel():
    data = str(distance_data) + " cm"
    distanceLeftData.configure(text=data)

def updateRightDataLabel():
    data = str(distance_data) + " cm"
    distanceRightData.configure(text=data)

# Update connected status
def setDisconnectedLabel():
    connectionStatusText.configure(bg="lightsalmon1", text=" Disconnected", width=10)

def setConnectedLabel():
    connectionStatusText.configure(bg="darkolivegreen2", text=" Connected", width=9)


def tellSlaveToSendData():
    print("sendData")
    data = createBinResult("0", "1111")
    server.tell_client(client, data)
    btDataReceived = server.listenForBTData(client)
    print("btDataReceived: ", btDataReceived)
    return


slavaDataButton = Button(buttonsFrame, text="Tell slave to\n send data", state=NORMAL, width=15, command=tellSlaveToSendData, font="Times 12", bg=buttonColor)
slavaDataButton.place(x=10, y=400)



# Stops sensorFrame from shrinking its parent, frame, to fit its size.
sensorFrame.pack_propagate(False)

sensorLabel = Label(sensorFrame, text="Unit Feedback", font="Times 18", bg=windowColor).pack()

################################## MAP #################################################################################
# This creates a canvas, and places it inside the frame. Frames are different from windows in that can be drawn in, which a window cannot. Will be useful for displaying the map later on.
mapWindow = Canvas(frame, width=400, height=400, bg="navajowhite1", highlightbackground=borderColor, highlightthickness=2)
mapWindow.place(x=25, y=25)

mapping.get_map(mapWindow)

def uppdate_map():
    mapping.get_map(mapWindow)

frame.mainloop()

server.end_session(client, local_server)

os.system('xset r on')



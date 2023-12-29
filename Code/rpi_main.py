#import communications.client as bt
#import spi.rpi_spi as spi
import communications.client as bt
import i2c.rpi_i2c as i2c
import time
import math

#float rightDist
#float leftDist
#float frontDist
#float rotationSpeed
#float traveledDist
#float currSpeed




def doAction(ID, val, bus):
    if ID == 0:
        #Gör inget
        i2c.writeData(i2c.styrningAddr, 0, bus)
    elif ID == 1:
        #Kör fram
        print("fram")
        i2c.writeData(i2c.styrningAddr, 1, bus)
    elif ID == 10:
        #Kör bak
        print("bak")
        i2c.writeData(i2c.styrningAddr, 2, bus)
    elif ID == 100:
        #rotera höger
        print("höger")
        i2c.writeData(i2c.styrningAddr, 3, bus)
    elif ID == 11:
        #Rotera vänster
        print("vänster")
        i2c.writeData(i2c.styrningAddr, 4, bus)
    elif ID == 5:
        pass
        #Kalibrera S. Vänster
    elif ID == 6:
        pass
        #-:- Höger
    elif ID == 7:
        pass
        #Kalibrera fram
    elif ID == 14:
        manualControl = True
    elif ID == 15:
        manualControl = False
    return 0



def bluetoothAction(client, data, bus):
    #Master = external, slave = rpi
    
    ID, val = bt.receiveData(client)

    if ID == 1111:
        print("Bomba send")
        bt.transferData(client, data)
        send = 0
    else:
        doAction(ID, val, bus)
        
def odometerToCm():
    return i2c.odometerCntr * 0.4555


def driveForward(targetDist, bus):
    i2c.resetOdometerCntr(bus)
    i2c.writeData(i2c.styrningAddr, 1, bus)
    f, r, l, g, o = i2c.getSensorData(bus)
    last_left = l
    last_right = r

    l_lower_lim = 10
    l_upper_lim = 13
    

    r_lower_lim = 10
    r_upper_lim = 13

    currDist = 0
    while(currDist < targetDist and f > 10):
        i2c.writeData(i2c.styrningAddr, 1, bus)
        time.sleep(0.01)
        f, r, l, g, o = i2c.getSensorData(bus)
        if(f == 0):   #bad solution, have to fix
            f = 11

        if( f < 10 ):
            break
           
        i2c.resetOdometerCntr(bus)

        if( not( l_lower_lim < l and l < l_upper_lim )):
            if (l < l_lower_lim):
                turnRight(2, bus)
            elif (l > l_upper_lim and r > r_upper_lim * 2):
                turnLeft(2, bus)
        
        if( not( r_lower_lim < r and r < r_upper_lim)):
            if(r < r_lower_lim):
                turnLeft(2, bus)
            elif(r > r_upper_lim and l > l_upper_lim * 2):
                turnRight(2, bus)

        f, r, l, g, o = i2c.getSensorData(bus)

    
def odometerToCm():
    return i2c.odometerCntr*0.4555


def degreesRotated(before, g):
    
    print(g)
    if g >= 125 and g <= 126:
        return 0
    return 3*(g - 125.5) * (time.perf_counter() - before)
    
    
def turnRight(targetDeg, bus):
    i2c.resetOdometerCntr(bus)
    i2c.writeData(i2c.styrningAddr, 3, bus)
    before = time.perf_counter()
    rotated = 0

    offset = targetDeg * 0.0277777      # to get a more correct turh
    
    while(rotated < targetDeg+offset):
        time.sleep(0.001)
        f, r, l, g, o = i2c.getSensorData(bus)
        rotated += degreesRotated(before, g)
        before = time.perf_counter()
        print("Rotated: ", rotated)
    i2c.writeData(i2c.styrningAddr, 0, bus)    



def turnLeft(targetDeg, bus):
    i2c.resetOdometerCntr(bus)
    i2c.writeData(i2c.styrningAddr, 4, bus)
    before = time.perf_counter()
    rotated = 0

    offset = targetDeg * 0.03333        # to get a more correct turn
    
    while(rotated < targetDeg -offset):
        time.sleep(0.001)
        f, r, l, g, o = i2c.getSensorData(bus)
        rotated -= degreesRotated(before, g)  # -= istället för += ty talet som returneras bör vara negativt.
        before = time.perf_counter()
        print("Rotated: ", rotated)
    i2c.writeData(i2c.styrningAddr, 0, bus)  

def degreesRotated(before, g):
    return (time.perf_counter() - before) * abs(g - 90)

def isFrontWall(bus):
    frontDistance = i2c.getSensorData(bus)[0]
    if frontDistance < 30:
        return True
    return False

def isRightWall(bus):
    rightDistance = i2c.getSensorData(bus)[1]
    if rightDistance < 30:
        return True
    return False

def isLeftWall(bus):
    leftDistance = i2c.getSensorData(bus)[2]
    if leftDistance < 30:
        return True
    return False

def main():
    
    running = True
    print("start")
    bus = i2c.initI2C()
    #client = bt.initClient()
    
    

 
    try:
        while(running):
    
            #sensorData = i2c.getSensorData(bus)
              
            driveForward(300, bus)
       
            time.sleep(0.5)
        
            #turnRight(180, bus)
        
            #time.sleep(0.5)
        
            #driveForward(300, bus)
            #time.sleep(0.5)
        
            turnLeft(85, bus)
            time.sleep(1)      
     

            #bluetoothAction(client, sensorData, bus)
    except KeyboardInterrupt:
        i2c.writeData(i2c.styrningAddr, 0, bus)

       

    i2c.closeBus()
    #bt.closeClient(client)
    print("connecion disabled")


main()



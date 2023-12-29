import smbus2
import time

styrningAddr = 0x50
sensorAddr = 0x60
manualControl = False
odometerCntr = 0

def initI2C():
    return smbus2.SMBus(1)
    
def closeBus(bus):
    bus.close()

def writeData(addr:int, data, bus) -> None:
    try:
        bus.write_byte(addr, data)
    except OSError as e: 
        print("i2c Write Error")
    return
    
def readData(sensor:int, bus):
    try:
        if(sensor == 0):
            return readByte(sensorAddr, bus) # readFront
        
        elif(sensor == 1):
            return readByte(sensorAddr, bus) # readRight
        
        elif(sensor == 2):
            return readByte(sensorAddr, bus) # readLeft
        
        elif(sensor == 3):
            return readByte(sensorAddr, bus) # readGyro
        
        elif(sensor == 4):   
            return readOdometer(bus)         # readOdometer
        else:
            print("readData, not a sensor")
    except OSError as e:
        print("i2c Read Error")
    return

def readOdometer(bus):
    global odometerCntr
    odometerCntr += readByte(sensorAddr, bus)
    return odometerCntr

def readByte(addr: int, bus):
    #print(addr)
    return bus.read_byte(addr)
    
    
def getSensorData(bus):
    sensorData = [0,0,0,0,0]
    for i in range(len(sensorData)):
        
        sensorData[i] = readData(i, bus)
        time.sleep(0.005)
    return sensorData
    
def resetOdometerCntr(bus):
    global odometerCntr
    odometerCntr = 0
    writeData(sensorAddr, 0, bus)
    time.sleep(0.005)
    
    

def test1():
    writeData(0x50, 0x00, [1, 2, 3])
    return

def test2():
    print(readData(0x50, 0, 3))
    return

def test3():
    print(readByte(0x50))
    return
    
#test1()
#test2()
#test3()


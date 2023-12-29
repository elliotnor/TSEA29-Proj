import time
import spidev


spi = spidev.SpiDev()
bus = 0
device = 0
styrningDevice = 0
sensorDevice = 1
import time

def setDevice(dev):
    """Device is the chip select pin. Set to 0 or 1, depending on the connections
    Device = 0 -> styrning
    device = 1 -> sensor"""
    if dev == styrningDevice:
        device = 0
    
    elif dev == sensorDevice:
        device = 1
    
    return

def enableSPI():
    """Open a connection to a specific bus and device (chip select pin)"""
    spi.open(bus, device)   
    return

def disableSPI():
    """Disconects the SPI device"""
    spi.close()
    return

def setSPIMode():
    """Sets SPI mode"""
    spi.mode = 0
    return

def setSPISpeed():
    """Set SPI transfer freq"""
    spi.max_speed_hz = 8000000
    return

def readData(n):
    """reads n bytes of data from the SPI device"""
    return spi.readbytes(n)

def writeData(data):
    """Writes n bytes of data to the SPI device"""
    spi.writebytes(data)
    return

def initSpi():
    enableSPI()
    setDevice(sensorDevice)
    setSPIMode()
    setSPISpeed()
    return

def test1():
    a = 0
    lst = [20, 20, 20, 20, 20]
    enableSPI()
    setDevice(sensorDevice)
    setSPIMode()
    setSPISpeed()
    while a != 1000:
        writeData(lst)
        a += 1
        time.sleep(0.0001)
    readData(lst)
    return

def test2():
    a = 0
    lst = [5, 1, 2, 3, 4, 5] #lst = [len(lst-1), a, b, c, ...]
    enableSPI()
    setDevice(sensorDevice)
    setSPIMode()
    setSPISpeed()
    while(1):
        writeData(lst)
        time.sleep(0.0001)
        z = readData(5)
        print(z)
        a += 1
    return

def test3():
    lst = [1, 2, 3, 4, 5]
    enableSPI()
    setDevice(sensorDevice)
    setSPIMode()
    setSPISpeed()

    while(1):
        writeData(lst)
        time.sleep(0.0001)
    return
    
    
    
def test4():
    a = 0
    lst = [5, 1, 2, 3, 4, 5] #lst = [len(lst-1), a, b, c, ...]
    enableSPI()
    setDevice(sensorDevice)
    setSPIMode()
    setSPISpeed()
    writeData(lst)
    time.sleep(0.0001)
    z = readData(5)
    print(z)
    a += 1
    return

#test1()
#test2()
test3()
#test4()

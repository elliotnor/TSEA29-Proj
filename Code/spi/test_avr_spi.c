//File 1

#include <avr/io.h>
#include <avr/interrupt.h>

// Function to initialize SPI Slave mode
void SPI_SlaveInit(void) {
	// Set MISO (PB6) as output
	DDRB |= (1 << DDB6);

	// Enable SPI, set as Slave, and enable interrupts
	SPCR |= (1 << SPE) | (1 << SPIE);
}

// Function to receive data from the master
uint8_t SPI_Receive(void) {
	// Wait for reception complete
	while (!(SPSR & (1 << SPIF)))
		
	// Return data register
	return SPDR;
}

// SPI interrupt vector
ISR(SPI_STC_vect) {
	PORTA = 0xff;
	// Read received data
	uint8_t receivedData = SPI_Receive();

	// Process received data as needed

	// Send a response back to the master
	SPDR = receivedData;
	//PORTA = 0;
}


int main(void) {
	// Initialize SPI Slave
	SPI_SlaveInit();
	DDRA |= 0xFF;
	// Enable global interrupts
	sei();

	while (1) {

	}

	return 0;
}




//File 2
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
    spi.max_speed_hz = 500000
    return

def readData(n):
    """reads n bytes of data from the SPI device"""
    return spi.readbytes(n)

def writeData(data):
    """Writes n bytes of data to the SPI device"""
    spi.writebytes(data)
    return

def transaction(data: list) -> list:
    return spi.xfer(data)
    
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
    lst = [20, 20, 20, 20, 20]
    enableSPI()
    setDevice(sensorDevice)
    setSPIMode()
    setSPISpeed()
    while(1):
        writeData(lst)
        time.sleep(0.0001)
        a += 1
    return

def test3():
    a = 0
    lst = [20, 20, 20, 20, 20]
    enableSPI()
    setDevice(sensorDevice)
    setSPIMode()
    setSPISpeed()
    while a != 10*100:
        t = transaction(lst)
        a += 1
        time.sleep(0.0001)
    return t


#test1()
test2()
#test3()
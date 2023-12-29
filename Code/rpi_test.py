#import communications.client as bt
#import spi.rpi_spi as spi
from communications.client import initClient
from communications.client import fetchData
from communications.client import closeClient
from spi.rpi_spi import initSpi
from spi.rpi_spi import writeData
from spi.rpi_spi import disableSPI

def main():
    
    running = True
    print("start")
    initSpi()
    while(running):
        ID = 1

        if ID == 0:
            #Gör inget
            pass
        elif ID == 1:
            #Kör fram
            print("fram")
            writeData([1])
        elif ID == 10:
            #Kör bak
            print("bak")
            writeData([2])
        elif ID == 100:
            #rotera höger
            print("höger")
            writeData([3])
        elif ID == 11:
            #Rotera vänster
            print("vänster")
            writeData([4])
        elif ID == 5:
            pass
            #Kalibrera S. Vänster
        elif ID == 6:
            pass
            #-:- Höger
        elif ID == 7:
            pass
            #-:- Fram
    disableSPI()
    print("connecion disabled")
main()
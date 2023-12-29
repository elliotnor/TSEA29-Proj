import socket
import i2c.rpi_i2c as i2c
import time


def initClient():
        
    client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    client.connect(("14:4F:8A:A8:BE:CE", 4)) #Edvards dator
    #client.connect(("54:14:F3:AB:30:1E", 4)) #Hugos dator
    return client
    
def closeClient(client):    
    client.close()
    return

def fetchData(client):        
    try:
        data = client.recv(1024)
        print(data)

    except OSError as e:
        print("OSError")
        return "0b1111111111111111"
    return data
    
def receiveData(client):
    data = fetchData(client)
    ID = int(data[1:5])
    val = int(data[8:15])
    
    return ID, val

def transferData(client, sensorData):
    print(sensorData)
    for i in range(len(sensorData)):
        client.send(bytes(str(sensorData[i]), 'UTF-8'))
        time.sleep(0.1)
    client.send(bytes('-1', 'UTF-8'))
    #client.send(bytes("hello", 'UTF-8'))
"""
def getRelevantData(bus):
    #TODO: Implement
    return i2c.getSensorData(bus)
"""
    


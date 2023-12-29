import socket 

import time

#import TSEA29_GUI

def setup_server():
    server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    server.bind(("14:4F:8A:A8:BE:CE", 4)) #Edvard dator
    #server.bind(("54:14:F3:AB:30:1E", 4)) #Hugo dator
    server.listen(1)
    client, addr = server.accept()
    return server, client, addr

def tell_client(client, message):
    try:
        client.send(repr(message).encode("utf-8"))
    except OSError as e:
        print("tellclient OSerror")
        pass

def listenForBTData(client):
    btDataList = []
    clbtData = 0
    try:
        while(int(clbtData) != -1):
            clbtData = client.recv(1024)
            print(int(clbtData))
            btDataList.append(int(clbtData))
        return btDataList[:-1]
        
    except OSError as e:
        print("listenForBtData OSerror")
        pass

def end_session(client, server):  
    client.close()
    server.close()
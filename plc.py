import snap7
from time import sleep

global plc
plc = snap7.client.Client()
plc.connect('192.168.x.x',0,1)      #Pripoji sa k PLC
def getLocation():
    location = plc.db_read(1,9,9)   #Precitanie aktualnej polohy
    return location
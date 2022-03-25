from display import *
from lightsensor import *
import time
from data import *

display.setup()
while True:
    checklight()
    temperature,pressure,humidity = readBME280All()
    now = datetime.datetime.now()
    datime=int(now.strftime("%S"))
    datime=datime*1.666666
    datime=int(datime)
    datime2=int(datime/10)
    print (datime2)
    print (datime)
    
    if datime == 51:
        store_data(temperature,pressure,humidity)
    
    if datime2==0 or datime2==1 or datime2==2:
        display.drawCLOCK()
        #time.sleep(1)
        
    if datime2==3 or datime2==4 or datime2==5:
        display.drawTEMP()
        #time.sleep(1)
    
    if datime2==6 or datime2==7:
        display.drawPRES()
        #time.sleep(1)
        
    if datime2==8 or datime2==9:
        display.drawHVAC()
        #time.sleep(1)

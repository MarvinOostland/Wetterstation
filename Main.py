from display import *
from lightsensor import *
import time

display.setup()
while True:
    checklight()
    now = datetime.datetime.now()
    datime=int(now.strftime("%S"))
    datime=datime*1.666666
    datime=int(datime/10)
    datime2=datime
    print (datime)
    
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

from display import *
from lightsensor import *
import time
from data import DataStorage

class Main(object):
    def __init__(self) -> None:
        display.setup()
        self.LED=18
        GPIO.setup(self.LED, GPIO.OUT)
        self.wert=100
        self.mode=1
        self.p = GPIO.PWM(18, 50)
        self.p.start(10)
        
    def calclight(self):
        lights=LightSensor().checklight()
        
        
        if lights<2000:
            if self.wert<100:
                self.wert=self.wert+10
            print(f'{str(self.wert)}%')
            self.disphigh(self.wert)
        
        if lights>2000:
            if self.wert>10:
                self.wert=self.wert-10
            print(f'{str(self.wert)}%')
            self.displow(self.wert)
            
    def disphigh(self, wert):
        self.p.ChangeDutyCycle(wert)

    def displow(self, wert):
        self.p.ChangeDutyCycle(wert)

    def run(self):
        while True:
            self.calclight()
            temperature,pressure,humidity = readBME280All()
            now = datetime.datetime.now()
            self.datime = int(now.strftime("%S"))
            self.datime *= 1.666666
            self.datime = int(self.datime)
            self.datime2 = self.datime // 10
            print (self.datime2)
            print (self.datime)

            if self.datime == 49:
                self.mode=1
            if self.datime == 51 and self.mode==1:
                DataStorage.store_data(temperature,pressure,humidity)
                self.mode=0
                print("save!")


            if self.datime2 in {0, 1, 2}:
                display.drawCLOCK()
                #time.sleep(1)

            if self.datime2 in {3, 4, 5}:
                display.drawTEMP()
                #time.sleep(1)

            if self.datime2 in {6, 7}:
                display.drawPRES()
                #time.sleep(1)

            if self.datime2 in {8, 9}:
                display.drawHVAC()
                #time.sleep(1)


if __name__ == "__main__":
    app = Main()
    app.run()
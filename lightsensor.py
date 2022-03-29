import RPi.GPIO as GPIO
import time

class LightSensor(object):
    def __init__(self) -> None:
        self.LED=18
        self.wert=100
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.LED, GPIO.OUT)
        self.p = GPIO.PWM(18, 50)
        self.p.start(0)
        self.pin_to_circuit = 23

    def rc_time (self, pin_to_circuit):
        count = 0

        GPIO.setup(pin_to_circuit, GPIO.OUT)
        GPIO.output(pin_to_circuit, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(pin_to_circuit, GPIO.IN)

        while (GPIO.input(pin_to_circuit) == GPIO.LOW):
            count += 1

        return count

    def disphigh(self):
        #wert=self.wert
        if self.wert<100:
            self.wert=self.wert+10
        print(f'{str(self.wert)}%')
        self.p.ChangeDutyCycle(self.wert)

    def displow(self):
        #wert=self.wert
        if self.wert>10:
            self.wert=self.wert-10
        print(f'{str(self.wert)}%')
        self.p.ChangeDutyCycle(self.wert)

    def checklight(self):
        #wert=self.wert
        pin_to_circuit=self.pin_to_circuit
        
        lights=self.rc_time(pin_to_circuit)
        print(lights)
        
        if lights<2000:
            self.disphigh()
        
        if lights>2000:
            self.displow()

#while True:
    #self.checklight()
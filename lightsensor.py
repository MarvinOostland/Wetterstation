import RPi.GPIO as GPIO
import time
from Main import*

class LightSensor(object):
    def __init__(self) -> None:
        
        
        #self.p.start(10)
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



    def checklight(self):
        lights=self.rc_time(self.pin_to_circuit)
        print(lights)
        return (lights)

import RPi.GPIO as GPIO
import time


LED=18
wert=100
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
p = GPIO.PWM(18, 50)
p.start(0)
pin_to_circuit = 23

def rc_time (pin_to_circuit):
    count = 0

    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin_to_circuit, GPIO.IN)

    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

def disphigh():
    global wert
    if wert<100:
        wert=wert+10
    print(str(wert)+"%")
    p.ChangeDutyCycle(wert)

def displow():
    global wert
    if wert>10:
        wert=wert-10
    print(str(wert)+"%")
    p.ChangeDutyCycle(wert)

def checklight():
    global wert
    global pin_to_circuit
    
    lights=rc_time(pin_to_circuit)
    print(lights)
    
    if lights<2000:
        disphigh()
    
    if lights>2000:
        displow()

#while True:
    #checklight()
    
    
    
    
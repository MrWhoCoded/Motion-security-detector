import RPi.GPIO as gpio
from time import sleep 
from datetime import datetime
import camera

pir = 7
led = 11

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(pir, gpio.IN)
gpio.setup(led, gpio.OUT)

state = None
status = True
counts = 0

try:
    while status:
        state = gpio.input(pir)
        sleep(0.8)
        if state == 1:
            counts += 1
            print(counts)
            if counts == 4:
                counts = 0
                print("Motion detected")
                with open("/home/pi/Desktop/programming/motion detector/time_stamps.txt", "r+") as file:
                    gpio.output(led, gpio.HIGH)
                    file.read()
                    file.write(str(datetime.now()) + "\n")
                    camera.capture_moment()
                gpio.output(led, gpio.LOW)
            else:
                pass
            
except KeyboardInterrupt:
    gpio.cleanup()
    print("exited")
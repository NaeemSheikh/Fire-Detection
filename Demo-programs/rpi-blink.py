import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

start = time.time()

def fire_alert(t):
    ct = time.time()
    if ct < (t+5):  
        GPIO.output(7,True)
        time.sleep(0.1)
    else:
        GPIO.output(7,False)
        
if __name__ == "__main__":
    state = False
    while True:
        x = random.random() 
	y = random.random() 
	z = x+y
	print z
        if z > 1.8:
            start = time.time()
        fire_alert(start)
        time.sleep(1)

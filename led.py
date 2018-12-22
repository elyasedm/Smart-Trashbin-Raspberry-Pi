#!/usr/bin/python
import RPi.GPIO as GPIO
import time ,sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
redPin = 26
greenPin = 19  
bluePin = 13  
GPIO_TRIGGER = 20
GPIO_ECHO = 21
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
def jarakbenda ():
    GPIO.output(GPIO_TRIGGER,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    timeout_counter = int(time.time())
    start = time.time()
    while GPIO.input(GPIO_ECHO) == 0 and (int(time.time()) - timeout_counter) < 3 :
	start = time.time()
    timeout_counter = int(time.time())
    stop = time.time()
    while GPIO.input(GPIO_ECHO) == 1 and (int(time.time()) - timeout_counter) < 3 :
	stop = time.time()
    elapse = stop - start 
    distance = elapse * 34320
    distance = distance / 2
    return distance
def blink(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
def turnOff(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
def redOn():
    blink(redPin)
def redOff():
    turnOff(redPin)
def greenOn():
    blink(greenPin)
def greenOff():
    turnOff(greenPin)
def blueOn():
    blink(bluePin)
def blueOff():
    turnOff(bluePin)
def yellowOn():
    blink(redPin)
    blink(greenPin)
def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)
def cyanOn():
    blink(greenPin)
    blink(bluePin)
def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)
def magentaOn():
    blink(redPin)
    blink(bluePin)
def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)
def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)
def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)
try:
    while True:
	GPIO.output(GPIO_TRIGGER, GPIO.LOW)
	jarak = jarakbenda()
	print ("Jarak benda = %.3f CM " % jarak)
	if jarak <= 25 :
	    redOn()
	    time.sleep(0.5)
	    redOff()
	    print("merah")

	elif jarak <= 50:
	    yellowOn()
	    time.sleep(0.5)
	    yellowOff()
	    print("kuning")

	elif jarak <= 75:
	    greenOn()
	    time.sleep(0.5)
	    greenOff()
	    print("hijau")

	elif jarak <= 100:    
	    cyanOn()
	    time.sleep(0.5)
	    cyanOff()
	    print("biru pantai")

	elif jarak <= 125:    
	    blueOn()
	    time.sleep(0.5)
	    blueOff()
	    print("biru")

	elif jarak <= 150:
	    magentaOn()
	    time.sleep(0.5)
	    magentaOff()
	    print("ungu")

	elif jarak > 150:
	    whiteOn()
	    time.sleep(0.5)
	    whiteOff()
	    print("putih")
except:
    p.stop()
    GPIO.cleanup()

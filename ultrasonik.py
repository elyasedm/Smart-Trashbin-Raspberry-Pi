#!/usr/bin/python
import RPi.GPIO as GPIO
import time ,sys
import lcddriver

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_TRIGGER_1 = 20
GPIO_ECHO_1 = 21

GPIO_BUZZER = 18
GPIO_SERVO = 16

GPIO_TRIGGER_2 = 7
GPIO_ECHO_2 = 8

display = lcddriver.lcd()

GPIO.setup(GPIO_TRIGGER_1, GPIO.OUT)
GPIO.setup(GPIO_ECHO_1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_2, GPIO.OUT)
GPIO.setup(GPIO_ECHO_2, GPIO.IN)

GPIO.setup(GPIO_SERVO, GPIO.OUT)
GPIO.setup(GPIO_BUZZER, GPIO.OUT)

p = GPIO.PWM(GPIO_SERVO,50)
p.start(2.5)

def jarakbenda1():
    GPIO.output(GPIO_TRIGGER_1,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_1,False)
    timeout_counter = int(time.time())
    start = time.time()
    while GPIO.input(GPIO_ECHO_1) == 0 and (int(time.time()) - timeout_counter) < 3 :
	start = time.time()
    timeout_counter = int(time.time())
    stop = time.time()
    while GPIO.input(GPIO_ECHO_1) == 1 and (int(time.time()) - timeout_counter) < 3 :
	stop = time.time()
    elapse = stop - start 
    distance = elapse * 34320
    distance = distance / 2
    return distance
    
def jarakbenda2():
    GPIO.output(GPIO_TRIGGER_2,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_2,False)
    timeout_counter = int(time.time())
    start = time.time()
    
    while GPIO.input(GPIO_ECHO_2) == 0 and (int(time.time()) - timeout_counter) < 3 :
	start = time.time()
    timeout_counter = int(time.time())
    stop = time.time()
    
    while GPIO.input(GPIO_ECHO_2) == 1 and (int(time.time()) - timeout_counter) < 3 :
	stop = time.time()
    elapse = stop - start 
    distance = elapse * 34320
    distance = distance / 2
    return distance

try:
    while True:
	GPIO.output(GPIO_TRIGGER_1, GPIO.LOW)
	jarak1 = jarakbenda1()
	GPIO.output(GPIO_TRIGGER_2, GPIO.LOW)
	jarak2 = jarakbenda2()
	print ("Jarak orang = %.3f CM " % jarak1)
	print ("Jarak sampah = %.3f CM " % jarak2)
	if jarak1 <= 25 :
	    display.lcd_display_string("  Smart Trash!", 1) # Write line of text to first line of display
            display.lcd_display_string("  Trash Opened ", 2) # Write line of text to second line of display
	    p.ChangeDutyCycle(9)
	    GPIO.output(GPIO_BUZZER,1)
	    time.sleep(1)
	    GPIO.output(GPIO_BUZZER,0)
	    time.sleep(2)
	else:
	    if jarak2 <= 5:
		display.lcd_display_string("  !!!!Full!!!!  ", 2) # Write line of text to second line of display
		p.ChangeDutyCycle(2.8)
		GPIO.output(GPIO_BUZZER,1)
		time.sleep(1)
            else :
		display.lcd_display_string("  Smart Trash!", 1) # Write line of text to first line of display
		display.lcd_display_string("  Trash Closed ", 2) # Write line of text to second line of display
		p.ChangeDutyCycle(2.8)
		GPIO.output(GPIO_BUZZER,0)
		time.sleep(1)
except:
    display.lcd_clear()
    p.stop()
    GPIO.cleanup()

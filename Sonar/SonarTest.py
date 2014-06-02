# Author _Magnus Johansson_
# Measuring distance with HC-SR04 ultrasonic Module

#importing necessary Python libraries
import time
import RPi.GPIO as GPIO

#using BCM GPIO reference
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 23
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

#make sure trigger isn't on
GPIO.output(GPIO_TRIGGER, False)

def measure():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    sent = time.time()
    while GPIO.input(GPIO_ECHO)==0:
        sent = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        returned = time.time()

    #Calculate time
    elapsed = returned-sent

    distance = elapsed * 34300 / 2

    print "Distance is : %.1f" % distance

# ultrasonic module needs a moment to settle in
time.sleep(0.5)
measure()

#reset GPIO
GPIO.cleanup()

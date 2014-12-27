#!/usr/bin/python
# Measuring distance with HC-SR04 ultrasonic Module
import time
import RPi.GPIO as GPIO
import Settings



def getDistance(sonarTrigger, sonarEcho):
    #using BCM GPIO reference
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sonarTrigger, GPIO.OUT)
    GPIO.setup(sonarEcho, GPIO.IN)

    GPIO.output(sonarTrigger, True)
    time.sleep(0.00001)
    GPIO.output(sonarTrigger, False)

    sent = time.time()

    time.sleep(0.5)

    while GPIO.input(sonarEcho)==0:
        sent = time.time()

    while GPIO.input(sonarEcho)==1:
        returned = time.time()

    #Calculate time
    elapsed = returned-sent

    distance = elapsed * 34300 / 2

    #reset GPIO
    GPIO.cleanup()
    return distance

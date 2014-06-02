#!/usr/bin/python
#PIR (motion) sensor - HC-SR501
import RPi.GPIO as GPIO
import sys
sys.path.append("/home/pi/surveillance-pi/")
import BoardNumbers as BoNu

sensorPin = BoNu.pirPort
print(sensorPin)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def getPirStatus():
  return GPIO.input(sensorPin)

#!/usr/bin/python
#PIR (motion) sensor - HC-SR501
import RPi.GPIO as GPIO
import Settings

GPIO.setmode(GPIO.BCM)

def getPirStatus(sensorPin):
  GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  return GPIO.input(sensorPin)

#!/usr/bin/python
import RPi.GPIO as GPIO

#Ignores any warning
GPIO.setwarnings(False)

# Alternatively use GPIO.BOARD to use board pin numbering
GPIO.setmode(GPIO.BCM)

global sonarEcho = 0
global sonarTrigger = 0

def sonarEchoPort():
  return sonarEcho

def sonarTriggerPort():
  return sonarTrigger

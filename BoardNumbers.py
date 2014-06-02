#!/usr/bin/python
import RPi.GPIO as GPIO

#Ignores any warning
GPIO.setwarnings(False)

# Alternatively use GPIO.BOARD to use board pin numbering
GPIO.setmode(GPIO.BCM)

sonarEcho = 24
sonarTrigger = 25
pir = 18

def sonarEchoPort():
  return sonarEcho

def sonarTriggerPort():
  return sonarTrigger

def pirPort():
  return pir

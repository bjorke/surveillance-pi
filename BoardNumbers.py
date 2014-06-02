#!/usr/bin/python
import RPi.GPIO as GPIO

#Ignores any warning
GPIO.setwarnings(False)

# Alternatively use GPIO.BOARD to use board pin numbering
GPIO.setmode(GPIO.BCM)

sonarEcho = 23
sonarTrigger = 24
pir = 18

def sonarEchoPort():
  return sonarEcho

def sonarTriggerPort():
  return sonarTrigger

def pirPort():
  return pir

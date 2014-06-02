#!/usr/bin/python
import BoardNumbers as BoNu
import sys
sys.path.append("/home/pi/surveillance-pi/Pir")
import Pir

sonarEcho = 0
sonarTrigger = 0
pirEcho = 0

def controlPir():
  intVal = Pit.getPirStatus(pirEcho)
  return intVal

if __name__ == "__main__":
  global sonarEcho
  global sonarTrigger
  global pirEcho
  sonarEcho = BoNu.sonarEchoPort()
  sonarTrigger = BoNu.sonarTriggerPort()
  pirEcho = BoNu.pirPort()

  print(controlPir())

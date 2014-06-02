#!/usr/bin/python
import BoardNumbers as BoNu
import sys
sys.path.append("/home/pi/surveillance-pi/Pir")
import Pir
sys.path.append("/home/pi/surveillance-pi/Sonar")
import Sonar

sonarEcho = 0
sonarTrigger = 0
pirEcho = 0

def getPirValue():
  return Pir.getPirStatus(pirEcho)

def getSonarDistance():
  return Sonar.getDistance(sonarTrigger,sonarEcho)

if __name__ == "__main__":
  sonarEcho = BoNu.sonarEchoPort()
  sonarTrigger = BoNu.sonarTriggerPort()
  pirEcho = BoNu.pirPort()

  print(getPirValue())
  print(getSonarDistance())

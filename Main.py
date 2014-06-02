#!/usr/bin/python
import BoardNumbers as BoNu
sonarEcho = 0
sonarTrigger = 0
pir = 0

def sonarEchoPort():
  intVal = BoNu.sonarEchoPort
  return intVal
def sonarTriggerPort():
  intVal = BoNu.sonarTriggerPort
  return intVal
def pirPort():
  intVal = BoNu.pirPort
  return intVal

if __name__ == "__main__":
  global sonarEcho = sonarEchoPort
  global sonarTrigger = sonarTriggerPort
  global pir = pirPort
  print(sonarEcho,sonarTrigger,pir)

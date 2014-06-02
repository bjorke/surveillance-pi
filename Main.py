#!/usr/bin/python
import BoardNumbers as BoNu
sonarEcho = 0
sonarTrigger = 0
pir = 0

if __name__ == "__main__":
  global sonarEcho = BoNu.sonarEchoPort
  global sonarTrigger = BoNu.sonarTriggerPort
  global pir = BoNu.pirPort
  print(sonarEcho,sonarTrigger,pir)

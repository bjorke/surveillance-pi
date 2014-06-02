#!/usr/bin/python
import BoardNumbers as BoNu
sonarEcho = 0
sonarTrigger = 0
pirEcho = 0


if __name__ == "__main__":
  global sonarEcho
  global sonarTrigger
  global pirEcho
  sonarEcho = BoNu.sonarEchoPort()
  sonarTrigger = BoNu.sonarTriggerPort()
  pirEcho = BoNu.pirPort()
  print(sonarEcho,sonarTrigger,pir)

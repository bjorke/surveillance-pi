#!/usr/bin/python
import BoardNumbers as BoNu
import sys
import threading
from threading import Thread, Event
import os
import time

sys.path.append(os.getcwd() + "/Pir")
import Pir
sys.path.append(os.getcwd() + "/Sonar")
import Sonar

#pin variabels
sonarEcho = 0
sonarTrigger = 0
pirEcho = 0
#for debugging
debugging = True

def getPirValue():
  if debugging:
    print("pir ehco; " , pirEcho)
  return Pir.getPirStatus(pirEcho)
def getSonarDistance():
  if debugging:
    print("sonar echo; " , sonarEcho)
  return Sonar.getDistance(sonarTrigger,sonarEcho)

#keeping track of the threads spawned
threadsArray = []
class startChildThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        if self.name == "sonar":
          print("Sonar; " , getSonarDistance())

        if self.name == "pir":
          print("Pir; " , getPirValue())

def mainThread():
  global threadsArray
  global sonarEcho
  global sonarTrigger
  global pirEcho
  sonarEcho = BoNu.sonarEchoPort()
  sonarTrigger = BoNu.sonarTriggerPort()
  pirEcho = BoNu.pirPort()
  threadOne = startChildThread(1, "sonar")
  threadTwo = startChildThread(2, "pir")

  if not threadOne.isAlive():
    threadOne.start()
    threadsArray.append(threadOne)
  if not threadTwo.isAlive():
    threadTwo.start()
    threadsArray.append(threadTwo)

  while True:
    for t in threadsArray:
      t.join()
    break

if __name__ == "__main__":
  mainThreadRun = Thread(target=mainThread , args=())
  for counter in range (0, 10):
    if not mainThreadRun.isAlive():
      mainThreadRun.start()
      wait(1)

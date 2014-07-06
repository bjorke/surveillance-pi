#!/usr/bin/python
import BoardNumbers as BoNu
import sys
import threading
from threading import Thread, Event

sys.path.append("/home/pi/surveillance-pi/Pir")
import Pir
sys.path.append("/home/pi/surveillance-pi/Sonar")
import Sonar

sonarEcho = 0
sonarTrigger = 0
pirEcho = 0

def getPirValue():
  print("pir ehco; " , pirEcho)
  return Pir.getPirStatus(pirEcho)
def getSonarDistance():
  print("sonar echo; " , sonarEcho)
  return Sonar.getDistance(sonarTrigger,sonarEcho)

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

if __name__ == "__main__":
   mainThreadRun = Thread(target=mainThread , args=())
   if mainThreadRun.isAlive():
     mainThreadRun.join()
   else:
     mainThreadRun.start()

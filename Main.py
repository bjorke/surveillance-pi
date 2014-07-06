#!/usr/bin/python
import BoardNumbers as BoNu
import sys
from threading import Thread, Event

sys.path.append("/home/pi/surveillance-pi/Pir")
import Pir
sys.path.append("/home/pi/surveillance-pi/Sonar")
import Sonar

sonarEcho = 0
sonarTrigger = 0
pirEcho = 0

threadsArray = []
class startChildThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        if self.name == "forward":


def getPirValue():
  return Pir.getPirStatus(pirEcho)

def getSonarDistance():
  return Sonar.getDistance(sonarTrigger,sonarEcho)
def mainThread():
  sonarEcho = BoNu.sonarEchoPort()
  sonarTrigger = BoNu.sonarTriggerPort()
  pirEcho = BoNu.pirPort()

  print("Pir; " , getPirValue())
  print("Sonar; " , getSonarDistance())
if __name__ == "__main__":
   mainThreadRun = Thread(target=mainThread , args=())
   #if mainThreadV.isAlive():
      #mainThreadV.join()
   #else:
   mainThreadRun.start()

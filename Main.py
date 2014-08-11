#!/usr/bin/python
#import BoardNumbers as BoNu
import RPi.GPIO as GPIO #to access the pins on the board
import sys
import threading
from threading import Thread, Event
import os
import time
import Settings
#Importing all the different hardware modules
sys.path.append(os.getcwd() + Settings.path["Pir"])
import Pir
sys.path.append(os.getcwd() + Settings.path["Sonar"])
import Sonar
sys.path.append(os.getcwd() + Settings.path["Camera"])
import Camera
#Ignores any warning
GPIO.setwarnings(False)
# Alternatively use GPIO.BOARD to use board pin numbering
GPIO.setmode(GPIO.BCM)
#pin variabels
sonarEcho = Settings.path["sonarEchoPort"]
sonarTrigger = Settings.path["sonarTriggerPort"]
pirEcho = Settings.path["pirPort"]
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
def getPicture():
  if debugging:
    print("taking pucture to path; ", Settings.path["imageStorage"])
  return Camera.takePicture()
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

        if self.name == "camera":
          print("camera" , getPicture())

def mainThread():
  global threadsArray

  threadOne = startChildThread(1, "sonar")
  threadTwo = startChildThread(2, "pir")
  threadThree = startChildThread(3, "camera")

  if not threadOne.isAlive():
    threadOne.start()
    threadsArray.append(threadOne)
  if not threadTwo.isAlive():
    threadTwo.start()
    threadsArray.append(threadTwo)
  if not threadThree.isAlive():
    threadThree.start()
    threadsArray.append(threadThree)

  while True:
    for t in threadsArray:
      t.join()
    break


if __name__ == "__main__":
  counter = 0
  mainThreadRun = Thread(target=mainThread , args=())

  while counter < 10:
    if not mainThreadRun.isAlive():
      mainThreadRun.start()
      counter += 1
      time.sleep(1)
      mainThreadRun.kill()

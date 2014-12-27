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
sys.path.append(os.getcwd() + Settings.path["pirModule"])
import Pir
sys.path.append(os.getcwd() + Settings.path["sonarModule"])
import Sonar
sys.path.append(os.getcwd() + Settings.path["cameraModule"])
import Camera
#Ignores any warning
GPIO.setwarnings(False)
# Alternatively use GPIO.BOARD to use board pin numbering
GPIO.setmode(GPIO.BCM)
#pin variabels
sonarEcho = Settings.pinNumbers["sonarEchoPort"]
sonarTrigger = Settings.pinNumbers["sonarTriggerPort"]
pirEcho = Settings.pinNumbers["pirPort"]
#for debugging
debugging = True

def getPirValue():
    return Pir.getPirStatus(pirEcho)
def getSonarDistance():

    return Sonar.getDistance(sonarTrigger,sonarEcho)
def getPicture():
    imagePath = os.getcwd() + Settings.path["imageStorage"]
    if debugging:
        print("taking pucture to path; ", imagePath)

    Camera.takePicture(imagePath,debugging)

#keeping track of the threads spawned
threadsArray = []
class startChildThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        if self.name == "sonar":
          print("sonar distance;",getSonarDistance())

        if self.name == "pir":
          print("pir; ",getPirValue())

        if self.name == "camera":
          getPicture()
    def cancel(self):
      self.thread.cancel()

def mainThread():
    global threadsArray

    threadOne = startChildThread(1, "sonar")
    #threadTwo = startChildThread(2, "pir")
    #threadThree = startChildThread(3, "camera")

    if not threadOne.isAlive():
        threadOne.start()
        threadsArray.append(threadOne)
    '''
    if not threadTwo.isAlive():
        threadTwo.start()
        threadsArray.append(threadTwo)
    if not threadThree.isAlive():
        threadThree.start()
        threadsArray.append(threadThree)
    '''
    while True:
        for t in threadsArray:
            t.join()
        break

if __name__ == "__main__":
    counter = 0

    while counter < 10:
        mainThreadRun = Thread(name="main thread",target=mainThread)
        if debugging:
            print("counter is; ",counter)
            print("checking if thread is alive; ",mainThreadRun.isAlive())
        if not mainThreadRun.isAlive():
            if debugging:
                print("starting main thread")
            mainThreadRun.start()
        counter += 1
        mainThreadRun.join(2)

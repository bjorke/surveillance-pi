#!/usr/bin/python
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

#output for pir
pirOutput = False

def pir ():
    prevState = False
    currState = False
    while True:
        time.sleep(0.1)
        prevState = currState
        currState =  Pir.getPirStatus(pirEcho)
        if currState != prevState:
            print("pit changed value")

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        if self.name == "pir":

        print ("thread; " , self.name)

threads = []
def handlerThread():
    # Create new threads
    thread1 = myThread(1, "pir")
    thread2 = myThread(2, "Thread-2")
    thread3 = myThread(3, "Thread-3")

    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Add threads to thread list
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)

    # Wait for all threads to complete
    for t in threads:
        t.join()

if __name__ == "__main__":
    handler = Thread(name="handlerThread",target=handlerThread)
    handler.start()

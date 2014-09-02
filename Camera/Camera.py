#!/usr/bin/python
#Raspberry PI camera module

import time
import picamera
import Settings

def takePicture():

  with picamera.PiCamera() as camera:
    camera.start_preview()
    #time.sleep(5)
    returnImage = camera.capture("image.jpg")
    camera.stop_preview()
    return returnImage

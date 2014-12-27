#!/usr/bin/python
#Raspberry PI camera module

import time
import picamera
import Settings

def takePicture():

    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        timeNow = time.strftime("%Y%m%d-%H%M%S")
        returnImage = camera.capture(timeNow + ".jpg")
        print("### IMAGE; ",returnImage)
        camera.stop_preview()
        return returnImage

#!/usr/bin/python
#Raspberry PI camera module

import time
import picamera
import Settings

def takePicture(folder):

    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        timeNow = time.strftime("%Y%m%d-%H%M%S")
        folderAndFile = folder + timeNow + ".jpg"
        print("save as; ",folderAndFile)
        returnImage = camera.capture(folderAndFile)
        camera.stop_preview()
        return returnImage

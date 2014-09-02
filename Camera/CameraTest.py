import time
import picamera
import Settings

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(5)
    camera.capture(Settings.pathTest["cameraModule"] + "image.jpg")
    camera.stop_preview()

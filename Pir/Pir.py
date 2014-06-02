import BoardNumbers as BoNu
BoardNumbers.path.append("~/surveillance-pi/")

sensorPin = BoNu.pirPort

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def getPirStatus():
  return GPIO.input(sensorPin)

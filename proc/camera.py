from picamera import PiCamera
from time import sleep

camera =PiCamera()
camera.resolution = (500,500)

def snap(filename, text):
    try:
        camera.annotate_text = text
        camera.start_preview()
        sleep(2)
        camera.capture(filename)
        camera.stop_preview()
    except:
        raise

    return 1

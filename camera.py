from picamera import PiCamera
import time

cam = PiCamera()
cam.vflip = True

def capture_moment():
    cam.start_preview()
    time.sleep(2)

    cam.start_recording("capture.h264")
    time.sleep(10)
    cam.stop_recording()
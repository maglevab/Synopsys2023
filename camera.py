#!/usr/bin/env python

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(10)
camera.capture('/tmp/picture1.jpg')
camera.stop_preview()

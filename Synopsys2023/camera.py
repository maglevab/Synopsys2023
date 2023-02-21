#!/usr/bin/env python

from picamera2 import Picamera2
from time import sleep

camera = Picamera2()
config = camera.create_preview_configuration(main={"size": (1600, 1200)})
camera.configure(config)
camera.capture_file('testImage.jpg')
camera.close()

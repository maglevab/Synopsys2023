import time
import shutil
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)


calibX = accelerometer.acceleration[0]
calibY = accelerometer.acceleration[1]
calibZ = accelerometer.acceleration[2]

currX = 0
currY = 0
currZ = 0

red = False
orange = False
green = False

while True:
	currX = abs( accelerometer.acceleration[0] - calibX)
	currY = abs( accelerometer.acceleration[1] - calibY)
	currZ = abs( accelerometer.acceleration[2] - calibZ)

	print(currX, currY, currZ)

	if (currX > 3.398375 and currX < 6.12875) or (currY > 3.398375 and currY < 6.12875) or (currZ > 0.5768571429 and currZ < 2.5435):
		orange = True
		shutil.copyfile("/var/www/html/index_orange.html", "/var/www/html/index.html")
	elif currX > 6.12875 or currY > 6.12875 or currZ > 2.5435:
		red = True
		shutil.copyfile("/var/www/html/index_red.html", "/var/www/html/index.html")
	else:
		green = True
		shutil.copyfile("/var/www/html/index_green.html","/var/www/html/index.html")

	if red == True:
		print("POWER POLE HAS FALLEN DOWN")
		break
	elif orange == True:
		print("POWER POLE HAS TILTED AND MAY FALL DOWN SOON")
	else:
		print("POWER POLE IS STABLE AND STANDING")

	time.sleep(0.5)

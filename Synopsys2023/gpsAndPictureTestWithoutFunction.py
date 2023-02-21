from gps3.agps3threaded import AGPS3mechanism
import time
from picamera import PiCamera
camera = PiCamera()

agps_thread = AGPS3mechanism()
agps_thread.stream_data()
agps_thread.run_thread()

while True:
	print('---------------------')
	speed = agps_thread.data_stream.speed
	print(speed)
#	print(agps_thread.data_stream.time)
#	print('Lat:{}   '.format(agps_thread.data_stream.lat))
#	print('Lon:{}   '.format(agps_thread.data_stream.lon))
#	print('Speed:{} '.format(agps_thread.data_stream.speed))
#	print('Course:{}'.format(agps_thread.data_stream.track))
	if speed != 'n/a':
		print("Speed is not n/a")
		print("speed is " +  str(speed) + " meters per second")
		print("speed being converted")
		speed = float(speed)
		speed *= 2.2369362920544
		print(speed)
		if float(speed) > 13:
			camera.capture('/home/pi/test_pics/picture' + str(speed) + ".jpg")
			print('PictureTaken')
		else:
			print('Picture Not Needed')
	print('---------------------')
	time.sleep(2)

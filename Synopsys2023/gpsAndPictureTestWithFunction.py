from gps3.agps3threaded import AGPS3mechanism
import time
from picamera import PiCamera
camera = PiCamera()


def checkSpeed(camera):

	agps_thread = AGPS3mechanism()  # Instantiate AGPS3 Mechanisms
	agps_thread.stream_data()  # From localhost (), or other hosts, by example, (host='gps.ddns.net')
	agps_thread.run_thread()  # Throttle time to sleep after an empty lookup, default '()' 0.2 two tenths  # All data is available via instantiated thread data stream attribute.
    # line #140-ff of /usr/local/lib/python3.5/dist-packages/gps3/agps.py
	print('---------------------')
	#print(                   agps_thread.data_stream.time)
	#print('Lat:{}   '.format(agps_thread.data_stream.lat))
	#print('Lon:{}   '.format(agps_thread.data_stream.lon))
	speed = agps_thread.data_stream.speed
	print(speed)
	#print('Course:{}'.format(agps_thread.data_stream.track))
	if speed != 'n/a':
		print("speed is n\a")
		if int(speed) > 13:
			#take picture
			camera.capture('/tmp/picture' + str(speed) + '.jpg')
			print('PictureTaken')
		else :
			print('Picture Not Needed')
	print('---------------------')
	time.sleep(0.5) # Sleep, or do other things for as long as you like.





from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from picamera import PiCamera
from time import sleep
import random

camera = PiCamera()

gauth = GoogleAuth()

# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'picture.jpg', 'parents': [{'id': '1iEBKVqaFh9iCgQzTA1Aotf8wnZwHWcwo'}]})
file1.SetContentFile('/home/pi/Synopsys2023/picsForAI/picture2006.jpg')
file1.Upload()

while True:
	#take picture
	camera.capture('/tmp/picture1.jpg')
	num = random.randit()

	file1.Trash()
	file2 = drive.CreatFile({'title' : 'picture' + str(num) + '.jpg','parents': [{'id': '1iEBKVqaFh9iCgQzTA1Aotf8wnZwHWcwo'}]}) 
	file2.SetContentFile('/tmp/picture1.jpg')
	file2.Upload()
	file1.SetContentFile(file2)
	print('uploaded picture'+num+'.jpg')

	time.sleep(10)


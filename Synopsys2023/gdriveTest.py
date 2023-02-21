from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

#file1 = drive.CreateFile({'title': 'picture.jpg', 'parents': [{'id': '1iEBKVqaFh9iCgQzTA1Aotf8wnZwHWcwo'}]})
file1 = drive.CreateFile({'id': '1-Tj9b6tMKSxXPnCj7Cf2phYGUw_wqcoE'})
file1.Trash()
'''
file1.SetContentFile('/home/pi/Synopsys2023/picsForAI/picture2006.jpg')
file1.Upload()

while True:
	#take picture

	file1.SetContentFile('/home/pi/Synopsys2023/picsForAI/picture2006.jpg')
	file1.Upload()


file1.SetContentFile('home/pi/Synopsys2023/picsForAI/picture2664.jpg')
file1.Upload()
'''

from picamera import PiCamera
from keras.models import load_model
from PIL import Image
import numpy as np

model = load_model('/home/pi/CNN_Model().h5')

camera = PiCamera()
camera.capture('/home/pi/picture.jpg')

test_image = Image.open('/home/pi/picture.jpg').convert('L')
test_image = test_image.resize((640, 480))
test_image = np.asarray(test_image)
test_image = test_image.resize(1, 640, 480, 1)

result = model.predict(test_image)
result2 = result.flatten()
resultList = result2.toList()
maxVal = max(result2)

if str(resultList.index(maxVal)) == '0':
	continue
else: 
	#play noise
	#send email

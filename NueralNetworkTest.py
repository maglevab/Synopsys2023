from keras.models import load_model
from PIL import Image
import numpy as np
import os
model = load_model("C:\\Users\\aesho\\Downloads\\SynopsysProject\\CNN_Model(~95%Acc).h5")
path = 'C:\\Users\\aesho\\Downloads\\picsForAI'
for file in os.listdir(path):
    test_image = Image.open(path+'\\'+str(file)).convert('L')
    test_image = test_image.resize((640, 480))
    #test_image.save('C:\\Users\\aesho\\Downloads\\picsForAI_Greyscale\\' + str(file) + 'Greyscale.jpg')
    test_image = np.asarray(test_image)
    test_image.resize(1, 640, 480, 1)


    result = model.predict(test_image)
    result2 = result.flatten()
    resultList = result2.tolist()
    maxVal = max(result2)
    if str(resultList.index(maxVal)) == '0':
        print('image ' + str(file) + ' is classified as not distracted')
    else:
        print('image ' + str(file) + ' is classified as distracted')

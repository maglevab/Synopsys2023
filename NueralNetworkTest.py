from keras.models import load_model
from PIL import Image
import numpy as np
import os

model = load_model("C:\\Users\\aesho\\Downloads\\SynopsysProject\\CNN_Model_Final.h5")
c0CorrectCounter = 0
c0PredictCounter = 0
c0TotalImages = 0
totalCorrectCounter = 0
totalImages = 0

for folder in os.listdir("C:\\Users\\aesho\\Downloads\\Synopsys2023Data\\newValidate"):
    for file in os.listdir("C:\\Users\\aesho\\Downloads\\Synopsys2023Data\\newValidate\\" + folder):

        test_image = Image.open("C:\\Users\\aesho\\Downloads\\Synopsys2023Data\\newValidate\\" + folder + "\\" + str(file)).convert('L')
        test_image = test_image.resize((640, 480))
        test_image = np.asarray(test_image)
        test_image.resize(1, 640, 480, 1)

        result = model.predict(test_image)
        print(result)
        result2 = result.flatten()
        resultList = result2.tolist()
        maxVal = max(result2)
        print(resultList.index(maxVal))
        if str(resultList.index(maxVal)) == '0':
            c0PredictCounter += 1
        if str(resultList.index(maxVal)) == folder[-1]:
            totalCorrectCounter += 1
            if str(resultList.index(maxVal)) == '0':
                c0CorrectCounter += 1
        totalImages += 1
        if folder == 'c0':
            c0TotalImages += 1

print("Accuracy between c0 and not c0 was " + str((c0CorrectCounter/c0PredictCounter)*100) + "%")
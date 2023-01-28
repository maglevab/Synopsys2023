import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
accelerometer.enable_motion_detection(threshold=18)
while True:
    x = accelerometer.acceleration[0]
    y = accelerometer.acceleration[1]
    z = accelerometer.acceleration[2]

    print(x, y, z)
    time.sleep(0.5)

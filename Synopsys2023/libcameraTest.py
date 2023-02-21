import subprocess

subprocess.run(['libcamera', '-jpeg', '-o', 'test.jpg', '-t 1000', '--width 640', '--height 480'])
#libcamera-jpeg -o test.jpg -t 1000 --width 640 --height 480


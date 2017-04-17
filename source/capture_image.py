import os
import time


def capture_image1():
    capture = os.system('fswebcam --device /dev/video0 /home/pi/FridgeAndLight/img/image1.jpg')
def capture_image2():
    capture = os.system('fswebcam --device /dev/video1 /home/pi/FridgeAndLight/img/image2.jpg')

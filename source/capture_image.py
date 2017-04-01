import sys
import os
import subprocess


def capture_image():
    capture = subprocess.Popen('fswebcam ../img/image.jpg')

from upload_dropbox import TransferData
from access_token import Token
from time import gmtime, strftime
import time
from get_image import get_image_path1
from get_image import get_image_path2
from capture_image import capture_image1
from capture_image import capture_image2

def dropbox_app():
    capture_image1()
    capture_image2()
    
    image_path1 = get_image_path1()
    image_path2 = get_image_path2()

    time_str = strftime("%Y-%m-%d-%H-%M-%S", gmtime())

    upload_path1 = '/Photos/{}1.jpg'.format(time_str)
    upload_path2 = '/Photos/{}2.jpg'.format(time_str)

    token = Token()
    access_token = token.get_access_token()

    uploader = TransferData(access_token)

    uploader.upload_file(image_path1, upload_path1)
    uploader.upload_file(image_path2, upload_path2)

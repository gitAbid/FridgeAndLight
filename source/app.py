from upload_dropbox import TransferData
from access_token import Token
from time import gmtime, strftime
from get_image import get_image_path
from capture_image import capture_image


capture_image()
image_path = get_image_path()

time_str = strftime("%Y-%m-%d %H:%M:%S", gmtime())

upload_path = '/FridgeAndLight/Image at {}'.format(time_str)

token = Token()
access_token = token.get_access_token()

uploader = TransferData(access_token)

uploader.upload_file(image_path, upload_path)



from upload_dropbox import TransferData
from token import get_access_token


image_path = '../test_files/current.png'
upload_path ='/FridgeAndLight/'
access_token = get_access_token()

uploader = TransferData(access_token)

uploader.upload_file(image_path, upload_path)


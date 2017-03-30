from upload_dropbox import TransferData
from access_token import Token


image_path = '../test_files/current.png'
upload_path ='/FridgeAndLight/current.png'

token = Token()
access_token = token.get_access_token()

uploader = TransferData(access_token)

uploader.upload_file(image_path, upload_path)


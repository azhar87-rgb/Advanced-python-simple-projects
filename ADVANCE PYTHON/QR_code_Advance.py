import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://www.youtube.com/@gbnature2261")
img=qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="blue")
img.save("GB_NATURE.jpg")
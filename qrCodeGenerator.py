# import qrcode as qr
# # Must use pip install pillow
# img=qr.make("https://www.youtube.com/@shehrmaindihat")
# img.save("Shermaindehat.png")

import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)
qr.add_data("https://www.youtube.com/@TaarakMehtaKaOoltahChashmah")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="black")
img.save("Black_Box.png")
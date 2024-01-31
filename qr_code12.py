import qrcode
from PIL import Image

qr =qrcode.QRCode(version = 1, 
                  error_correction = qrcode.constants.ERROR_CORRECT_H,
                  box_size=20,border=4)
qr.add_data("https://pkmc.tu.edu.np/")
qr.make(fit=True)
img = qr.make_image(fill_color="blue",back_color="white")
img.save("Padmakanya_Campus.png")
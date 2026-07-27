import os
import qrcode


def generate_qr(data,fill_color,back_color,filename):

    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size =10,
    border = 4
)
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color = fill_color,
        back_color = back_color
    )

    os.makedirs("Output",exist_ok=True)

    image.save(f"Output/{filename}.png")


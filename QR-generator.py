import qrcode

# URL to be made into a QR
data = "https://www.example.com"

# QRcode Class
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

# Add data to the instance 'qr'
qr.add_data(data)
qr.make(fit=True)

# Create the QR image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR as a png
img.save("QR.png")
